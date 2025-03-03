# Adaptive Thresholding
#  Thresholding value is calculated for a smaller region, not a global values

# need
# different regions of the image may have different lighting conditions
# so the different regions require diffrent threshold value

import cv2
img=cv2.imread('./Images/img2.jpg',0)

th=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

# adaptiveThreshold(image, maxvales, thresholding method, thresholding type, block size, cvalue)
th=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

# there are two types of thresholding methods
# 1 cv2.ADAPTIVE_THRESH_MEAN_C: takes the mean of all the values in the neighbourhood of block size and minus cvalues

# 2 cv2.ADAPTIVE_THRESH_GAUSSIAN_C: we have the gaussain mask of size as block size and aplly it to calculate the value minus cvalue 

_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow('Image3',th2)
cv2.imshow('Image2',th)
cv2.imshow('Image1',img)
cv2.waitKey(0)



