import cv2
import numpy as np
# Template Matching
# - method to find the smaller portion(template) in the larger image

img=cv2.imread('./Images/img1.jpg',0)
template=cv2.imread('./Images/img6.jpg',0)

result=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
# now where this template matches with the image the top left corner is the brightest and the remaining are darker values
# 
# find the brightest value
threshold=.985
loc=np.where(result>=threshold)
# print(loc)
# print(result)

w,h=template.shape
for i in range(len(loc[0])):
    cv2.rectangle(img,(loc[1][i],loc[0][i]),(loc[1][i]+h,loc[0][i]+w),(0,255,0),2)
cv2.imshow('Image',img)
cv2.imshow('Template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()