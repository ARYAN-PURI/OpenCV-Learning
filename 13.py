# thresholding: is a very powerful segmentation technique used for separating a object from its background
# it involves comaparing each pixel of image with predefined threshold value

# it divides the image pixels into two groups
# pixels > threshold
# pixels < threshold

# cv2.threshold(img,threshold,maxvalues,type of thresholding)

# cv2.THRESH_BINARY => 0 if p<threshold else 1

# cv2.THRESH_BINARY_INV => 0 if p<threshold else 1

# cv2.THRESH_TRUNC => p if p<threshold else threshold

# cv2.THRESH_TOZERO => 0 if p<threshold else p

# cv2.THRESH_TOZERO_INV => p if p<threshold else 0