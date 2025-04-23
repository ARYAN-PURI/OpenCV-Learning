# Hough Transform
# The Hough Transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. 
# It can detect the shape even if it is broken or distorted a little bit. 

# basics

# Cartesian Coordinates System

# Y=MX+C 

# if you have a line in XY plane then that is represented as a point in MC plane
# if you have a point in XY plane then that is represented as a line in MC plane
# 
# so we have a no of points on the line in XY plane
# then plotting them on MC plane gives corresponding lines
# and intersection of all these line have a point that represent the single line passing through them


# Polar Coordinates System

# R=XCosQ + YSinQ
# (R is perpendicular diatance from from orgin and Q is the angle it makes with x axis)

# if you have a line in XY plane similarly represented as a pont in RQ plane
# if we have point in XY plane then it is represented as a form of sine cosine curve in RQ plane

# since cartesian coordinates system can not represent vertical lines so we use polar coordinates

# Hough transformation Algorithm 
# • 1. Edge detection, e.g. using the Canny edge detector. 
# • 2. Mapping of edge points to the Hough space and storage in an accumulator. 
# • 3. Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints. 
# • 4. Conversion of infinite lines to finite lines
 

# Hough Lines Method
import cv2
import numpy as np
img=cv2.imread('./Images/suduko.jpg',0)
img=cv2.resize(img,(512,512))
edges=cv2.Canny(img,200,220)


lines=cv2.HoughLines(edges,1,np.pi/180,200)

cv2.imshow('Image',img)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
