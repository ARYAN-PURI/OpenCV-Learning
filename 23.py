import cv2
import numpy as np

# Read and resize the images
img1 = cv2.imread('Images/img1.jpg')
img2 = cv2.imread('Images/img2.jpg')
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Direct blending of two images
img12 = np.zeros((512, 512, 3), dtype=np.uint8)
img12[:, :256] = img1[:, :256]
img12[:, 256:] = img2[:, 256:]

cv2.imshow('Direct Blending', img12)

# ---------------------------
# Pyramid blending steps:
# 1. Find Gaussian pyramids
# ---------------------------
gp_img1 = [img1]
gp_img2 = [img2]

for i in range(6):
    gp_img1.append(cv2.pyrDown(gp_img1[-1]))
    gp_img2.append(cv2.pyrDown(gp_img2[-1]))

# ---------------------------
# 2. Find Laplacian pyramids
# ---------------------------
lp_img1 = [gp_img1[-1]]
lp_img2 = [gp_img2[-1]]

for i in range(6, 0, -1):
    size = (gp_img1[i - 1].shape[1], gp_img1[i - 1].shape[0])
    laplacian1 = cv2.subtract(gp_img1[i - 1], cv2.pyrUp(gp_img1[i], dstsize=size))
    laplacian2 = cv2.subtract(gp_img2[i - 1], cv2.pyrUp(gp_img2[i], dstsize=size))
    lp_img1.append(laplacian1)
    lp_img2.append(laplacian2)

# ---------------------------
# 3. Merge pyramids
# ---------------------------
img12_pyramid = []
for l1, l2 in zip(lp_img1, lp_img2):
    rows, cols, _ = l1.shape
    temp = np.zeros((rows, cols, 3), dtype=np.uint8)
    temp[:, :cols // 2] = l1[:, :cols // 2]
    temp[:, cols // 2:] = l2[:, cols // 2:]
    img12_pyramid.append(temp)

# ---------------------------
# 4. Reconstruct the final blended image
# ---------------------------
img12final = img12_pyramid[0]
for i in range(1, 7):
    size = (img12_pyramid[i].shape[1], img12_pyramid[i].shape[0])
    img12final = cv2.pyrUp(img12final, dstsize=size)
    img12final = cv2.add(img12final, img12_pyramid[i])

# Display the final blended image
cv2.imshow('Pyramid Blending Result', img12final)

cv2.waitKey(0)
cv2.destroyAllWindows()
