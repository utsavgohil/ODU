import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sam.jpg',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()