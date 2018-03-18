import cv2
import numpy as np	

# 44 0 0
# 84 115 255
img = cv2.imread('slika3.jpg')
bgnd = cv2.imread('background.jpg')

img2 = cv2.subtract(img,bgnd)
#outputImage = np.where(img == (10,255,10), bgnd, img)

cv2.imshow('1',img2)
#cv2.imshow('2',outputImage)

	
	
cv2.waitKey(0)