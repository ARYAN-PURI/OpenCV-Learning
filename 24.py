# contours
# - curve joining all the countinous points on the boundary have same intensity
# - used in object detection and recogonition

import cv2

img=cv2.imread('./Images/img4.webp',0)
edges=cv2.Canny(img,50,100)

_,thres=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)
# findContours helps to find out the contours in the imgae
# contours is a python list of all contours, each is a numpy array having cordinates of boundary points in the object
# heirarchy is vector contain the info about image topology
# findCountours(<image>,<contour finding mode>,<contour finding method>)

contours,hierarchy=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# No of contours
print(len(contours))
# First Contours
print(contours[0])

# to draw the contours
# drawContours(<imageon which to be drawn>,<contours array>,<index no of contour to draw>,<color>,<thickness>)
cv2.drawContours(img,contours,-1,0,3)

cv2.imshow('Image',img)
cv2.imshow('Edges',edges)
cv2.imshow('Binary',thres)
cv2.waitKey(0)
cv2.destroyAllWindows()