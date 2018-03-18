import cv2
import time

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_BRIGHTNESS,50)
#cap.set(cv2.CAP_PROP_CONTRAST,)
#cap.set(cv2.CAP_PROP_SATURATION,)
#cap.set(cv2.CAP_PROP_HUE,)
#cap.set(cv2.CAP_PROP_GAIN,)
#cap.set(cv2.CAP_PROP_EXPOSURE,)

img = cap.read()[1]
height,width = img.shape[:2]
print height,width
while True:
	img = cap.read()[1]
	
	height,width = img.shape[:2]
	cv2.line(img,(width/2-1,0),(width/2-1,height),(0,255,0),2)
	cv2.imshow('img', img)
	cv2.waitKey(1)
	#print "a"
