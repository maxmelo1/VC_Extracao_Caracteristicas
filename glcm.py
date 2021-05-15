import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy

def glcm(image, d=(1,0)):
    offset = {0: (1,0), 45: (1,1), 90: (0,1), 135: (-1, 1), 180: (-1, 0), 225: (-1,-1), 270: (0, -1), 315: (1,-1) }

    assert len(image.shape) == 2, "expected mxn shaped np array"
    assert type(d) == tuple and d[1] in [0, 45, 90, 135, 180, 225, 270, 315], "invalid seek angle"

    (width, height) = image.shape
    

    m = np.amax(image)
    c = np.zeros( (m,m) )

    offset_x = offset[d[1]][0]*d
    offset_y = offset[d[1]][1]*d
    off = offset[d[1]]*d[0]

    for y in range(height):
        for x in range(width):
            try:
                row = image[x,y]
                i = (x+off[0],y+ off[1])
                col = image[i]
                c[row, col] += 1
            except:
                pass
    
    aux = np.sum(c>0)
    print(aux)
    
    return c



img = Image.open('imgs/Lenna.png').convert('L')
img = np.array(img)



c = glcm(img)

# plt.imshow(img, cmap='gray')
# plt.show()

plt.imshow(c, cmap='gray')
plt.show()