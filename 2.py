import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

rows=256
cols=256
# use numpy to create a matrix for new image
image=np.ones((rows,cols),dtype=np.uint8)

# use matplot to plot the graphs
hr=[5]*255
hb=[10]*255

# plot two functions in single graph
plt.plot(hr)
plt.plot(hb)
# x values are index
# y values are hr[index]
plt.show()

# math library consist of pow, sine ,cos, tan, log and extra mathematical functions