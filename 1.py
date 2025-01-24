import cv2
import numpy

# check version
# print(cv2.__version__)

# Read the image
image=cv2.imread('./Images/img2.jpg',1)
# second argument is a flag 
# 1 IMREAD_COLOR
# 0 IMREAD_GRAYSCALE
# -1 IMREAD_UNCHANGED (including the alpha channel)

# if image does not exist return none

print(image)

# show image window name, image variable
cv2.imshow('Display Window',image)

# wait to image before disappear

# no of miliseconds to hold
# 0 means wait a lot
# also track which key is pressed

key=cv2.waitKey(5000)

# destroy all windows that we have created
if key==27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite('./Images/img2_copy.png',image)
# write an image in the form a file

    








