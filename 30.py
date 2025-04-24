import cv2
import numpy as np
img=cv2.imread('./Images/suduko.jpg',0)
img=cv2.resize(img,(512,512))
def findmedian(img,size):
    rows,cols=img.shape
    Nimg=img.copy()
    for i in range(int(size/2),rows-int(size/2)):
        for j in range(int(size/2),cols-int(size/2)):
            temp=np.zeros(size*size,dtype=int)
            for p in range(size):
                for q in range(size):
                    temp[(p*size)+q]=img[i + (p-int(size/2))][j + (q-int(size/2))]
            temp.sort()
            Nimg[i][j]=temp[int((size*size)/2)]
    return Nimg

Nimg=findmedian(img,3)
cv2.imshow('Image',img)
cv2.imshow('Median Image',Nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()