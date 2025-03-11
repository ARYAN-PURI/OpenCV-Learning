import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret, frame1=cap.read()
ret, frame2=cap.read()


while(cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)

    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    blur=cv2.GaussianBlur(gray,(3,3),0)

    _,thres=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    dilated=cv2.dilate(thres,None,iterations=3)

    contours, hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        (x,y,w,h)=cv2.boundingRect(i)
        if(cv2.contourArea(i)<10000):
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)


    if(ret):
        cv2.imshow('Video',frame1)
    if(cv2.waitKey(1)==27):
        break

    frame1=frame2
    ret,frame2=cap.read()
cv2.destroyAllWindows()
cap.release()