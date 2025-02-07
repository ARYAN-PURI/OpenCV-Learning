import cv2

img1=cv2.imread('./Images/img1.jpg',1)
img2=cv2.imread('./Images/img2.jpg',1)

img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

# Adding two images should have same size
# cv2.add(img1,img2) and their corresponding pixel values and prevent overflow by capping at 255

img3=cv2.add(img1,img2)

# add the images according to their weights
# cv2.addWeighted(img1,alpha,img2,beta,gamma)

# output=img1*alpha + img2*beta + gamma

# alpha → how much of the first image to retain
# beta → how much of the second image to retain

img4=cv2.addWeighted(img1,0.2,img2,0.7,0)

# Bitwise operations on images
# AND
img5=cv2.bitwise_and(img1,img2)

# Or
img6=cv2.bitwise_or(img1,img2)

# Not
img7=cv2.bitwise_not(img1)

# XOR
img8=cv2.bitwise_xor(img1,img2)

cv2.imshow('Image',img8)
cv2.waitKey()
cv2.destroyAllWindows()

