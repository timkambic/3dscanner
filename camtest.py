import cv2
import numpy as np	
def nothing(x):
	pass
cap0 = cv2.VideoCapture(1)
#cap1 = cv2.VideoCapture(1)
#cap2 = cv2.VideoCapture(2)
cv2.namedWindow('range_')
cv2.createTrackbar('range','range_',220,255,nothing)
cv2.createTrackbar('kernel','range_',0,7,nothing)
while True:
	img0 = cap0.read()[1]
	img_red=img0[:,:,2]
	range_val = cv2.getTrackbarPos('range','range_')
	print range_val
	thresh=cv2.inRange(img_red,range_val,255);
	cv2.imshow('threshold',thresh)
	kernel_val = cv2.getTrackbarPos('kernel','range_')
	if kernel_val > 0:
		kernel = np.ones((kernel_val,1),np.uint8)
		opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
		cv2.imshow('opening', opening)
	else: 
		cv2.imshow('opening',thresh)
	#img1 = cap1.read()[1]
	#cv2.imshow('1',img1)

	#img2 = cap2.read()[1]
	#cv2.imshow('2',img2)
	
	cv2.waitKey(1)