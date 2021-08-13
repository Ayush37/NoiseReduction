import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
import numpy as np
import os
import cv2
import math
from scipy.signal import convolve2d
#Load the image
def estimate_noise(I):
  H, W = I.shape

  M = [[1, -2, 1],
       [-2, 4, -2],
       [1, -2, 1]]

  sigma = np.sum(np.sum(np.absolute(convolve2d(I, M))))
  sigma = sigma * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))

  return sigma
print ("##### Running MEDIAN filter on different noises #### ")
image = cv2.imread('images/Gauss_Ayush_Marriage.jpg')
# Generate Gaussian noise
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
before_quality = estimate_noise(image2)
print ("Estimating quality for guassian image before median filter %8.4f " % (before_quality) )
figure_size = 9
new_image = cv2.medianBlur(image2,figure_size)
after_quality = estimate_noise(new_image)
print ("Estimating quality for guassian image after median filter %8.4f \n " % (after_quality))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Median filter')
plt.xticks([]), plt.yticks([])
plt.show()


image = cv2.imread('images/poisson_Ayush_Marriage.jpg')
# Generate Gaussian noise
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
before_quality = estimate_noise(image2)
print ("Estimating quality for poisson image before median filter  %8.4f" % (before_quality))
figure_size = 9
new_image = cv2.medianBlur(image2,figure_size)
after_quality = estimate_noise(new_image)
print ("Estimating quality for poisson image after median filter  %8.4f \n" % (after_quality))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Median filter')
plt.xticks([]), plt.yticks([])
plt.show()

image = cv2.imread('images/S&P_Ayush_Marriage.jpg')
# Generate Gaussian noise
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
before_quality = estimate_noise(image2)
print ("Estimating quality for S&P image before median filter  %8.4f" % (before_quality))
figure_size = 9
new_image = cv2.medianBlur(image2,figure_size)
after_quality = estimate_noise(new_image)
print ("Estimating quality for S&P image after median filter  %8.4f \n " % (after_quality))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Median filter')
plt.xticks([]), plt.yticks([])
plt.show()

image = cv2.imread('images/speckle_Ayush_Marriage.jpg')
# Generate Gaussian noise
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
before_quality = estimate_noise(image2)
print ("Estimating quality for speckle image before median filter  %8.4f" % (before_quality))
figure_size = 9
new_image = cv2.medianBlur(image2,figure_size)
after_quality = estimate_noise(new_image)
print ("Estimating quality for speckle image after median filter  %8.4f \n" % (after_quality))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Median filter')
plt.xticks([]), plt.yticks([])
plt.show()
