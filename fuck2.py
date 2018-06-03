
# show a pixel value
from skimage import io,data 
import matplotlib.pyplot as plt 
import numpy as np 
img=io.imread('0413.jpg') 
io.imshow(img)

rows,cols,dims=img.shape
#half = np.matrix([[0, 128],[192, 64]])
half = np.matrix([[0,128,32,160],[192,64,224,96],[48,176,16,144],[240,112,208,80]])
img2=img[:,:,:]
for i in range(0,rows): 
    for j in range(0,cols):
        for k in range(0,3):
            index_i = i%4 #2
            index_j = j%4 #2
            if img2[i,j,k] > half[index_i, index_j]:
                img2[i,j,k] = 255 
            else:
                img2[i,j,k] = 0
plt.figure()
io.imshow(img2)
io.show()