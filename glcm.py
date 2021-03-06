import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def glcm(image, d=(1,0), bits=8):
    offset = {0: (1,0), 45: (1,1), 90: (0,1), 135: (-1, 1), 180: (-1, 0), 225: (-1,-1), 270: (0, -1), 315: (1,-1) }

    assert len(image.shape) == 2, "expected mxn shaped np array"
    assert type(d) == tuple and d[1] in [0, 45, 90, 135, 180, 225, 270, 315], "invalid seek angle"

    (width, height) = image.shape
    

    #m = np.amax(image)
    m = 2**bits
    c = np.zeros( (m,m) )

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
    
    return c

def glcm_norm(image, d=(1,0), bits=8):
    c = glcm(image, d, bits)

    c = c / np.sum(c)
    
    return c

def energy(c):
    return np.sum(c**2)

def contrast(c):
    (width, height) = c.shape
    aux = [(lin-col)**2*c[lin, col] for lin in range(height) for col in range(width)]

    return np.sum(aux)

def entropy(c):
    (width, height) = c.shape
    eps = 0.00001
    aux = [c[lin, col]*np.log(c[lin,col]+eps) for lin in range(height) for col in range(width)]

    return np.sum(aux)

def homogeneity(c):
    (width, height) = c.shape
    aux = [c[lin, col]/(1+abs(lin-col)) for lin in range(height) for col in range(width)]

    return np.sum(aux)

def get_features(c):
    return [energy(c), contrast(c), entropy(c), homogeneity(c)]


img = Image.open('imgs/Lenna.png').convert('L')
img = np.array(img)



c = glcm(img)
c_norm = glcm_norm(img)

# plt.imshow(img, cmap='gray')
# plt.show()

plt.imshow(c, cmap='gray')
plt.title('GLCM')
plt.show()

plt.imshow(c_norm, cmap='gray')
plt.title('Normalized GLCM')
plt.show()

print(get_features(c_norm))

# print(c[50:80,50:120])
# print('---')
# print(c_norm[50:80,50:120])