import cv2
import numpy as np;
import matplotlib.pyplot as plt

# Image Gradients:
# - directional change in the intensity of an image
img=cv2.imread('Images/img1.jpg',0)

# Laplacian gradient
lap=cv2.Laplacian(img,cv2.CV_64F)

# cv2.CV_64F: 64 bit float to deal with floats and -ve.
lap=np.uint8(np.absolute(lap))
# converting them into unsigned int of 8 bits

# Sobel gradients

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelY=np.uint8(np.absolute(sobelY))

# dx=order of derivative x
# dy=order of derivative y

sobelcombined=cv2.bitwise_or(sobelX,sobelY)


titles=['Image','Laplacian','SobelX','SobelY','Combined']
images=[img,lap,sobelX,sobelY,sobelcombined]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'grey')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()