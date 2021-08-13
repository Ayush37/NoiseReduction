import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
#%matplotlib inline
import numpy as np
import os
import cv2
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 1
      var = 0.1
      sigma = var**5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 1
      amount = 0.05
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 255

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 50 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
   elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy

img = cv2.imread('images/Ayush_Marriage.jpg')
noisy_img = noisy('gauss', img)
cv2.imwrite('images/Gauss_Ayush_Marriage.jpg', noisy_img)
noisy_img = noisy('s&p', img)
cv2.imwrite('images/S&P_Ayush_Marriage.jpg', noisy_img)
noisy_img = noisy('poisson', img)
cv2.imwrite('images/poisson_Ayush_Marriage.jpg', noisy_img)
noisy_img = noisy('speckle', img)
cv2.imwrite('images/speckle_Ayush_Marriage.jpg', noisy_img)
