import cv2
import numpy as np
def cov(image,mask):
    rows,cols=image.shape
    blank=np.zeros((rows,cols),dtype=np.int16)
    m,n=mask.shape
    for i in range(int(m/2),rows-int(m/2)):
        for j in range(int(n/2),cols-int(n/2)):
            result=0
            for p in range(m):
                for q in range(n):
                    result+=mask[p][q]*image[i+(p - int(m/2))][j+(q - int(n/2))]
            blank[i][j]=result
    return blank

def thresholding(image, val):
    rows, cols=image.shape
    nimage=np.zeros((rows,cols),dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            if(image[i][j]>=val):
                nimage[i][j]=255
    return nimage
def normalize(image):
    rows,cols=image.shape
    max=0
    min=255
    for i in range(rows):
        for j in range(cols):
            if(image[i][j]>max):
                max=image[i][j]
            if(image[i][j]<min):
                min=image[i][j]
    
    newimage=np.zeros((rows,cols),dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            newimage[i][j]=round(255*((image[i][j]-min)/(max-min)))
    return newimage

img=cv2.imread('./Images/img1.jpg',0)
img=cv2.resize(img,(512,512))
mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
newimage=cov(img,mask)
secondimage=thresholding(normalize(newimage),135)
nimage=cv2.subtract(img,secondimage)
cv2.imshow('Image1',img)
cv2.imshow('Image3',secondimage)
cv2.imshow('Image4',nimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

