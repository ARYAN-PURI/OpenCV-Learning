import cv2
import numpy as np

def dillation(img,SE):
    rows,cols=img.shape
    m,n=SE.shape
    Nimg=np.zeros((rows,cols),dtype=np.uint8)

    for i in range(int(m/2), rows-int(m/2)):
        for j in range(int(n/2), cols-int(n/2)):
            sum=0
            for p in range(m):
                for q in range(n):
                    sum+=SE[p][q]*img[i + (p- int(m/2))][j + (q- int(n/2))]
            
            if(sum>0):
                Nimg[i][j]=255
    return Nimg

def errosion(img,SE):
    rows,cols=img.shape
    m,n=SE.shape
    Nimg=np.zeros((rows,cols),dtype=np.uint8)

    for i in range(int(m/2), rows-int(m/2)):
        for j in range(int(n/2), cols-int(n/2)):
            sum=0
            for p in range(m):
                for q in range(n):
                    sum+=SE[p][q]*img[i + (p- int(m/2))][j + (q- int(n/2))]
            
            if(sum==1275):
                Nimg[i][j]=255
    return Nimg
img=cv2.imread('./Images/suduko.jpg',0)
img=cv2.resize(img,(512,512))
rows,cols=img.shape
binaryimg=np.ones((rows,cols),dtype=np.uint8)*255
for i in range(rows):
    for j in range(cols):
        if(img[i][j]>127):
            binaryimg[i][j]=0

SE=np.array([[0,1,0],[1,1,1],[0,1,0]])
cv2.imshow('Image',binaryimg)
dilatedimg=dillation(binaryimg,SE)
errodedimg=errosion(binaryimg,SE)
cv2.imshow('Dillated Image',dilatedimg)
cv2.imshow('Erroded Image',errodedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
