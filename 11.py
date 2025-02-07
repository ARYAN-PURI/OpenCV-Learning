# Track Bars are used to change the values in the image during run time
import cv2
import numpy as np

img=np.zeros((512,512,3),dtype=np.uint8)
cv2.namedWindow('Image')

# x is current position of trackbar
def nothing(x):
    print(x)


# creating a trackbar
# createTrackbar(trackbar-name,window-name,initial-value,final-value,callback-fun(called when trackbar value changes))
cv2.createTrackbar('B','Image',0,255,nothing)
cv2.createTrackbar('G','Image',0,255,nothing)
cv2.createTrackbar('R','Image',0,255,nothing)

cv2.createTrackbar('OFF/ON','Image',0,1,nothing)

while(1):
    cv2.imshow('Image',img)
    if(cv2.waitKey(1)==27):
        break
    b=cv2.getTrackbarPos('B','Image')
    g=cv2.getTrackbarPos('G','Image')
    r=cv2.getTrackbarPos('R','Image')
    switch=cv2.getTrackbarPos('OFF/ON','Image')

    if(switch==1):
        img[:]=[b,g,r]
        # set all the values of img with a tuple


cv2.destroyAllWindows()