import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import time
import sys
from visual import *
#
#cam_laser_angle = 45
# Sin = 0.70710678118
multiplier =1/ 0.70710678118

# hold the value at which the scanning object currently is 0-359deg
object_angle =0

scalePoints = 0.3

scene2 = display(title='Live scan',x=0, y=0, width=600, height=400, background=(0.7,0.7,0.7),center=(0,0,100))
arrow(pos=vector(0,0,0), axis=vector(100,0,0),color = color.red,shaftwidth=1)
arrow(pos=vector(0,0,0), axis=vector(0,100,0),color = color.green,shaftwidth=1)
arrow(pos=vector(0,0,0), axis=vector(0,0,300),color = color.blue,shaftwidth=1)


img = cv2.imread('slika2.png')
img2 = img.copy()
height, width = img.shape[:2]
print height, width
cv2.line(img,(width/2-1,0),(width/2-1,height),(0,255,0),2) # draw center of the image
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV) # convert to hsv 

obj_color_low = np.array([0,0,0])  # lower end of laser color
obj_color_high = np.array([180,255,247]) # higher end of laser color

img2 = cv2.inRange(img2, obj_color_low, obj_color_high) # find laser line
img2 = cv2.bitwise_not(img2) # might not be necesarry

nSteps = 67 # number of vertical steps  (mogoce fajn da je visina deljiva s temu)
vertical_step = height/nSteps 
timestr = time.strftime("%Y%m%d-%H%M%S")
text_output = open("outputs/Output_"+timestr+".asc", "w")

time.sleep(1)

	
for fi in range(36):
	position = 0 # starting postion of vertical scann, starts at top
	for i in range(nSteps):
		nOkPixels = 0
		for x in range(width):
			if img2[position,x] > 0 and nOkPixels <1:
				cv2.circle(img,(x, position), 1, (255,0,0), -1)
				nOkPixels +=1
				# convert from pixel position to polar coordinate system
				D = width/2 - x 
				r = D*multiplier
				# polar to cartesian
				radians = math.radians(object_angle)
				xk = r * math.cos(radians)
				yk = r * math.sin(radians)
				zk = height-position
				#ax.scatter(xk, yk, zk)
				text_output.write(str(xk)+" "+str(yk)+" "+str(zk)+"\n")
				#print xk,yk,zk
				point_pos = [(int(xk)*scalePoints,int(yk)*scalePoints,int(zk)*scalePoints)]
				#print point_pos
				rate(100)
				points(pos=point_pos, size=2, color=color.red)
				#time.sleep(1)
				break;
		position+=vertical_step

	print object_angle
	object_angle+=10
	
text_output.close()

#cv2.imshow('range',img2)
#cv2.imshow('org',img)
cv2.waitKey(0)
cv2.destroyAllWindows()