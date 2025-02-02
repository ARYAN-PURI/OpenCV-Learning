import cv2
import numpy as np

img=cv2.imread('./Images/img2.jpg',0)
img=cv2.resize(img,(512,512))
cv2.imshow('Image',img)
rows=img.shape[0]
cols=img.shape[1]

img2=np.zeros((rows*2,cols*2),dtype=np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
for i in range(0,rows,30):
    for j in range(0,cols,30):
        img2=cv2.putText(img2,str(img[i][j]),(j+200,i+50),font,0.4,(255))
    print('\n')

cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.imwrite('./Images/img3.jpg',img)



cv2.destroyAllWindows()