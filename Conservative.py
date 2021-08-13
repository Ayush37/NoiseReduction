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

def conservative_smoothing_gray(data, filter_size):
    temp = []
    
    indexer = filter_size // 2
    
    new_image = data.copy()
    
    nrow, ncol = data.shape
    
    for i in range(nrow):
        
        for j in range(ncol):
            
            for k in range(i-indexer, i+indexer+1):
                
                for m in range(j-indexer, j+indexer+1):
                    
                    if (k > -1) and (k < nrow):
                        
                        if (m > -1) and (m < ncol):
                            
                            temp.append(data[k,m])
                            
            temp.remove(data[i,j])
            
            
            max_value = max(temp)
            
            min_value = min(temp)
            
            if data[i,j] > max_value:
                
                new_image[i,j] = max_value
            
            elif data[i,j] < min_value:
                
                new_image[i,j] = min_value
            
            temp =[]
    
    return new_image.copy()

image = cv2.imread('images/S&P_Ayush_Marriage.jpg')
# Generate Gaussian noise
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
before_quality = estimate_noise(image2)
print ("Estimating quality for guassian image before Conservative filter %8.4f " % (before_quality) )
figure_size = 9

new_image = conservative_smoothing_gray(image2,5)
after_quality = estimate_noise(new_image)
print ("Estimating quality for guassian image  after Conservative filter %8.4f " % (after_quality) )
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Conservative Smoothing')
plt.xticks([]), plt.yticks([])
#plt.show()

