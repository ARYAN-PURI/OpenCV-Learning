import cv2
# module to get date and time of the system
import datetime as dt
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    # datetime.now() return data in time format convert into string
    datetime=str(dt.datetime.now())
    frame=cv2.putText(frame,datetime,(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3)
    cv2.imshow('Video',frame)
    if(cv2.waitKey(1)==27):
        break
cap.release()
cv2.destroyAllWindows()