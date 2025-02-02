import cv2
# convert all the functions in cv2 into a dictory
a=dir(cv2)
for i in range(len(a)):
    # to print all the Events events
    if(a[i].find('EVENT')!=-1):
        print(a[i])

# we can use these events to make use of mouse click on the image

# mouse_event function basically deals with mouse events performed
# arg = event (type of event) , x,y = (cordinates of the event)
def mouse_event(event,x,y,flags,params):
    if(event==cv2.EVENT_LBUTTONDOWN):
        font=cv2.FONT_HERSHEY_COMPLEX
        text=str(x) + ', ' + str(y)
        
        # we create the copy of the image so the orignal image can be used for further click
        tempimg=img.copy()
        cv2.putText(tempimg,text,(x,y),font,0.5,(0,0,0))
        cv2.imshow('Image',tempimg)

img=cv2.imread('./Images/img1.jpg',1)
cv2.imshow('Image',img)

# setMouseCallback is a function that used to call the mouse_event function on a specifiedc image Window
cv2.setMouseCallback('Image',mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

