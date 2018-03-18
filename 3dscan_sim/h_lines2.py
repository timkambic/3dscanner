import cv2
import numpy as np

img_org = cv2.imread('slika3.png')
img = cv2.cvtColor(img_org,cv2.COLOR_BGR2HSV) 
obj_color_low = np.array([0,0,0])  # lower end of laser color
obj_color_high = np.array([180,255,247]) # higher end of laser color

img = cv2.inRange(img, obj_color_low, obj_color_high) # find laser line
img = cv2.bitwise_not(img) # might not be necesarry
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(img,1,np.pi/90,200,minLineLength,maxLineGap)
print""
print "len "+ str(len(lines))
print lines
print lines[0]
for i in range(0,len(lines)):
	print i
	# print lines[i]
	# x1 = lines[i][0]
	# print x1
	x1,y1,x2,y2 = lines[0][i]
	cv2.line(img_org,(x1,y1),(x2,y2),(2,2,2),2)
	
cv2.imshow('idk',img)
cv2.imshow('org',img_org)
#cv2.imshow('edges',edges)
cv2.imwrite('houghlines3.jpg',img)
cv2.waitKey(0)