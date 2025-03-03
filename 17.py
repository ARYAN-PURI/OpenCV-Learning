import matplotlib.pyplot as plt
import cv2
img=cv2.imread('Images/img1.jpg',1)

# matplot reads the image as rgb format
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

# showing multiple images in a single window in matplot

titles=['Image1','Image2']
images=[img,img1]

for i in range(2):
    plt.subplot(1,2,i+1)
    # subplot function define the layout of the window
    # plt.subplot(rows,cols,current image index)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.show()
cv2.waitKey(0)