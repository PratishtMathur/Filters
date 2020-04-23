import cv2
import cv2 as cv
import numpy as np

img = cv2.imread('images/jp.jpg')

scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
#The average blur
blur = cv.blur(image,(5,5))

#Gaussian Blur
gaus=cv.GaussianBlur(image,(5,5),0)

#Median Blur
#Useful for salt and pepper noise removal
med=cv.medianBlur(image,5)

#Bilateral Blur
#Useful for the removal of sharp edges
bil= cv.bilateralFilter(image,9,75,75)

img_concat = np.concatenate((image,blur,gaus,med,bil), axis=0)
cv2.imshow("Comparison",img_concat)
'''cv2.imshow("Original", image)
cv2.imshow("AVG BLUR", blur)
cv2.imshow("GAUSSIAN BLUR", gaus)
cv2.imshow("MEDIAN BLUR", med)
cv2.imshow("BILATERAL BLUR", bil)
'''
