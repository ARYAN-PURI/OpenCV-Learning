# Image Pyramids
# - Images of diffrent resolution
# - repeated smoothing and subsampling

# Types of Image Pyramids
# Gaussian Pyramids
# - repeat filtering and subsampling of images

import cv2
import numpy as np
img=cv2.imread('Images/img1.jpg',0)

# pyrDown
lr1=cv2.pyrDown(img)
# reduce the size of the image to 1/4th
lr2=cv2.pyrDown(lr1)

# pyrUp
hr1=cv2.pyrUp(lr2)
# increses the size of the image to 4 times

# Laplacian pyramids
# - created through gaussian pyramid

gp1=cv2.subtract(img,cv2.pyrUp(cv2.pyrDown(img)))
cv2.imshow('Image',gp1)

# layer=img.copy()
# gp=[layer]
# for i in range(5):
#     cv2.imshow('Image'+str(i+1),layer)
#     layer=cv2.pyrDown(layer)
#     gp.append(layer)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Need is to blend the images and reconstruction of the images.
