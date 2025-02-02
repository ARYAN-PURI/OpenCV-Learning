import cv2
import numpy as np

# drawing the line on the image using mouse click events
def event_mouse(event,x,y,flags,params):
    if(event==cv2.EVENT_LBUTTONDOWN):
        # thickness =-1 fill the circle or any closed shape
        tempimg=img.copy()
        cv2.circle(img,(x,y),2,(0,0,0),-1)
        points.append((x,y))
        if(len(points)>1):
            x1,y1=points[len(points)-2]
            x2,y2=points[len(points)-1]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,0),1)
        cv2.imshow('Image',img)

        # to show the color of the clicked pixel on the second window
        blue=tempimg[y][x][0]
        green=tempimg[y][x][1]
        red=tempimg[y][x][2]

        colorimg=np.ones((256,256,3),dtype=np.uint8)*[blue,green,red]
        cv2.imshow('ColorImage',colorimg)
        cv2.waitKey(1000)
        cv2.destroyWindow('ColorImage')



img=cv2.imread('./Images/img1.jpg',1)
cv2.imshow('Image',img)
points=[]
cv2.setMouseCallback('Image',event_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()