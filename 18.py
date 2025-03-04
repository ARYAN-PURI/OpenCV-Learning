import cv2
import matplotlib.pyplot as plt
import numpy as np

# Morphological Transformations
# - are some simple opeartions based on the image shape
# - are normally performed on binary images

#  we require two things 1) Image 2)Kernel

img=cv2.imread('Images/img4.webp',0)
_, mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((3,3),dtype=np.uint8)
dilation=cv2.dilate(mask,kernel,iterations=10)
# Dilation:
#  - which essentially increases the size of foreground objects (white pixels) in the image by expanding their boundaries
#  - effectively making them appear larger and thicker
#  - this is achieved by using a structuring element (kernel) to examine neighboring pixels and set a pixel to 'on' if at least one pixel within the kernel is 'on'. 

errosion=cv2.erode(mask,kernel,iterations=3)
# Errosion:
#  - similar to soil errosion as the soil is eroded on boundaries
#  - within the kernel if all the pixels are not ones then set center to zero
#  - used to shrik the shape of objects to separate to closely connected objects

openning=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# Opening: 
# - which essentially means it first erodes the image followed by a dilation

closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
# Closing: 
# - which essentially means it first dilute the image followed by a erosion

gradient=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
# gradient: 
#  - essentially highlighting the outlines of objects within the image 
#  - by taking the difference between the image after dilation and the image after erosion
#  - effectively revealing the boundaries of foreground objects. 

th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

images=[img,mask,dilation,errosion,openning,closing,gradient,th]
titles=['Images1','mask','Dilation','Errosion','openning','closing','gradient','th']
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
