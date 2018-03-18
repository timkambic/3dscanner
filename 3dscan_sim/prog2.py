import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import time
import sys
from visual import display,arrow,rate,points,vector,color
#
#cam_laser_angle = 45
# Sin = 0.70710678118
multiplierAngle =1/ 0.70710678118

# hold the value at which the scanning object currently is 0-359deg
object_angle =0

#scale down all point so they fit display
scalePoints = 0.3

# how many points to skip when displaying live 
# uses to much RAM otherwise
# if =2 it will skip 2 points
skipDrawingPoints = 3

# make window to display live data from scan
# add coordinate axis
scene2 = display(title='Live scan',x=0, y=0, width=600, height=400, background=(0.7,0.7,0.7),center=(0,0,100))
arrow(pos=vector(0,0,0), axis=vector(100,0,0),color = color.red,shaftwidth=1)
arrow(pos=vector(0,0,0), axis=vector(0,100,0),color = color.green,shaftwidth=1)
arrow(pos=vector(0,0,0), axis=vector(0,0,300),color = color.blue,shaftwidth=1)


img = cv2.imread('slika2.png')
img2 = img.copy()
height, width = img.shape[:2]
print height, width
# draw line where the center of scan table should be
cv2.line(img,(width/2-1,0),(width/2-1,height),(0,255,0),2) # draw center of the image

img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV) # convert to hsv 

# threshold laser out of the image
laser_low = np.array([0,0,0])  # lower end of laser color
laser_high = np.array([180,255,247]) # higher end of laser color
img2 = cv2.inRange(img2, laser_low, laser_high) # find laser line
img2 = cv2.bitwise_not(img2) # might not be necesarry

nSteps = 67*2 # number of vertical steps (number of vertical points)  (mogoce fajn da je visina deljiva s temu)
vertical_step = height/nSteps  

timestr = time.strftime("%Y%m%d-%H%M%S")
text_output = open("outputs/Output_"+timestr+".asc", "w") #Output file for coordinates of all points

time.sleep(1)


for fi in range(360):
	position = 0 # starting postion of vertical scann, starts at top
	drawPoint = skipDrawingPoints-1
	for i in range(nSteps):
		nOkPixels = 0
		for x in range(width):
			if img2[position,x] > 0 and nOkPixels <1:
				cv2.circle(img,(x, position), 1, (255,0,0), -1)
				nOkPixels +=1
				# convert from pixel position to polar coordinate system
				D = width/2 - x 
				r = D*multiplierAngle
				# polar to cartesian
				radians = math.radians(object_angle)
				xk = r * math.cos(radians)
				yk = r * math.sin(radians)
				zk = height-position
				# write x,y,z to output file
				text_output.write(str(xk)+" "+str(yk)+" "+str(zk)+"\n")
				#print xk,yk,zk
				point_pos = [(int(xk)*scalePoints,int(yk)*scalePoints,int(zk)*scalePoints)]
				#print point_pos
				drawPoint+=1
				if drawPoint == skipDrawingPoints:
					rate(500)
					r=i/67.0
					g=fi/360.0
					b=fi/360.0
					#print r,g,b
					points(pos=point_pos, size=2, color=(r,g,b))
					drawPoint=0
				#time.sleep(1)
				break;
		position+=vertical_step

	#print object_angle
	object_angle+=1
	
text_output.close()

#cv2.imshow('range',img2)
#cv2.imshow('org',img)
cv2.waitKey(0)
cv2.destroyAllWindows()