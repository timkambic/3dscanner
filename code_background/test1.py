import cv2
import numpy as np	

# 44 0 0
# 84 115 255
img = cv2.imread('slika2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('1',img)

	
	
cv2.waitKey(0)