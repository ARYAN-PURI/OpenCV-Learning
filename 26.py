import cv2

img=cv2.imread('./Images/img4.webp',1)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thres=cv2.threshold(grey,248,255,cv2.THRESH_BINARY_INV)
contours,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for i in contours:
    approx=cv2.approxPolyDP(i,0.01*cv2.arcLength(i,True),True)
    if(cv2.contourArea(approx)<700):
        continue
    cv2.drawContours(img,[approx],0,(0,255,0),2)

    if(len(approx)==3):
        print('Triangle')
    elif(len(approx)==4):
        print('Rectangle')
    elif(len(approx)==5):
        print('Pentagon')
    else:
        print('Circle')

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
