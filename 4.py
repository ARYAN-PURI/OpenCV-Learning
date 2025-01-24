import cv2
import numpy as np
# rgb image
image=np.ones((256,256,3),dtype=np.uint8)*255

# draw a line
# line(source, pt1, pt2, color in BGR, thickness)
image=cv2.line(image,(0,0),(200,200),(255,0,0), 5)

# arrowed line
image=cv2.arrowedLine(image,(10,0),(210,200),(0,255,0), 5)

# draw rectangle(source,top left vertex,loweer right vertex, color, thickness( -1 to fill inside))
image=cv2.rectangle(image,(0,0),(200,200),(0,0,255),5)

# draw circle(source, centre, radius, color thickness)
image=cv2.circle(image,(100,100),50,(255,0,0),-1)

# put text in image
# putText(source,text,starting point of text,font face,font size, color, thickness,line type)
font=cv2.FONT_HERSHEY_COMPLEX
image=cv2.putText(image,'Hello',(50,50),font,2,(255,0,0))
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()