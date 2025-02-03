import cv2
img =cv2.imread('./Images/img1.jpg',1)

# shape attribute gives the rows, cols, channels in the image
print(img.shape)

# size attribute will give the rows*cols*channels
print(img.size)

# dtype attribute will give the data type of the image
print(img.dtype)

# to split the image into three channels we use cv2.split()
# so that we can gather it in the form of tuple og BGR
b,g,r=cv2.split(img)

# now we have BGR channels so to merge them we use cv2.merge function
img2=cv2.merge((b,g,r))

# to work with the region of Interest in the image , we can get that in some another variable
roi=img[200:300,200:300]
# this is NumPy Slicing that help us to obtain the rectangular portion of the image
# ranging of rows(200-300) and cols(200-300)

img[100:200,100:200]=roi
cv2.imshow('Image',img)
cv2.waitKey()
cv2.destroyAllWindows()