import unittest
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

class TestStringMethods(unittest.TestCase):

    def estimate_noise(self,I):
      H, W = I.shape

      M = [[1, -2, 1],
           [-2, 4, -2],
           [1, -2, 1]]

      sigma = np.sum(np.sum(np.absolute(convolve2d(I, M))))
      sigma = sigma * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))
    
      return sigma

    def test_mean1(self):

        image = cv2.imread('/home/circleci/project/images/Gauss_Ayush_Marriage.jpg')
        # Generate Gaussian noise
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        before_quality = self.estimate_noise(image2)
        figure_size = 9
        new_image = cv2.blur(image2,(figure_size, figure_size))
        after_quality = self.estimate_noise(new_image)
        self.assertGreater(before_quality, after_quality)

    def test_mean2(self):

        image = cv2.imread('/home/circleci/project/images/poisson_Ayush_Marriage.jpg')
        # Generate Gaussian noise
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        before_quality = self.estimate_noise(image2)
        figure_size = 9
        new_image = cv2.blur(image2,(figure_size, figure_size))
        after_quality = self.estimate_noise(new_image)
        self.assertGreater(before_quality, after_quality)

    def test_mean3(self):

        image = cv2.imread('/home/circleci/project/images/S&P_Ayush_Marriage.jpg')
        # Generate Gaussian noise
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        before_quality = self.estimate_noise(image2)
        figure_size = 9
        new_image = cv2.blur(image2,(figure_size, figure_size))
        after_quality = self.estimate_noise(new_image)
        self.assertGreater(before_quality, after_quality)

    def test_mean4(self):

        image = cv2.imread('/home/circleci/project/images/speckle_Ayush_Marriage.jpg')
        # Generate Gaussian noise
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        before_quality = self.estimate_noise(image2)
        figure_size = 9
        new_image = cv2.blur(image2,(figure_size, figure_size))
        after_quality = self.estimate_noise(new_image)
        self.assertGreater(before_quality, after_quality)


if __name__ == '__main__':
    unittest.main()
