import cv2
import numpy as np

# Object Detection using HSV Color Space
# HSV color model helps to separate the color information from the luminiscence
cv2.namedWindow('Image')

def nothing(x):
    pass
img=cv2.imread('./Images/img4.webp',1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h,s,v values are mapped into 0-255

cv2.createTrackbar('UH','Image',255,255,nothing)
cv2.createTrackbar('US','Image',255,255,nothing)
cv2.createTrackbar('UV','Image',255,255,nothing)
cv2.createTrackbar('LH','Image',0,255,nothing)
cv2.createTrackbar('LS','Image',0,255,nothing)
cv2.createTrackbar('LV','Image',0,255,nothing)

cv2.imshow('image1',img)
while(True):
    uh=cv2.getTrackbarPos('UH','Image')
    us=cv2.getTrackbarPos('US','Image')
    uv=cv2.getTrackbarPos('UV','Image')
    lh=cv2.getTrackbarPos('LH','Image')
    ls=cv2.getTrackbarPos('LS','Image')
    lv=cv2.getTrackbarPos('LV','Image')

    lower=np.array([lh,ls,lv])
    upper=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower,upper)
    img2=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('image2',img2)
    if(cv2.waitKey(1)==27):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

