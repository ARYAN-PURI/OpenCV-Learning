import cv2
import numpy as np;
import matplotlib.pyplot as plt

# Smoothing or blurring of images:
# - helps to reduce noise from the image
# - linear filters

#  Homogeneous filter - mean filter
img=cv2.imread('Images/img1.jpg',1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),dtype=np.float32)*(1/25)

dst=cv2.filter2D(img,-1,kernel)
# each channel of rgb is processed separately

# ddepth: It is the desirable depth of destination image.
# - Value -1 represents that the resulting image will have same depth as the source image

blur=cv2.blur(img,(3,3))
# applying averaing and blurring effect

# Using Gaussian function also causing smoothing effect
gblur=cv2.GaussianBlur(img,(3,3),0)

# Median filter 
mfilter=cv2.medianBlur(img,5 )

# Bilateral Filter
# - removes the noise without blurring the edges
bifilter=cv2.bilateralFilter(img,9,75,75)

titles=['Image','2d Conv','Blur','Gaussian Blur','median filter','Bilateral filter']
images=[img,dst,blur,gblur,mfilter,bifilter]

for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
