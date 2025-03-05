import cv2
# Canny Edge Detection

#  - is an edge detection , multi-stage algorithm to detect wide range of edges in images
#  - steps
#  - Noise Reduction
#  - Gradient Calculation
#  - Non-maximum suppression (supress superious edges)
#  - Double Thresholding
#  - Edge Tracking by Hysteresis (fing single edge pixels)

img=cv2.imread('Images/img1.jpg',0)
canny=cv2.Canny(img,100,200,)

def nothing(x):
    print(x)

cv2.namedWindow('Image1')
cv2.createTrackbar('T1','Image1',0,255,nothing)
cv2.createTrackbar('T2','Image1',0,255,nothing)

while(1):
    t1=cv2.getTrackbarPos('T1','Image1')
    t2=cv2.getTrackbarPos('T2','Image1')
    canny=cv2.Canny(img,t1,t2)
    cv2.imshow('Image',canny)
    if(cv2.waitKey(1)==27):
        break
cv2.destroyAllWindows()

