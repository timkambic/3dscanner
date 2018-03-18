import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import time
import sys
#
#cam_laser_angle = 45
# Sin = 0.70710678118
multiplier =1/ 0.70710678118

# hold the value at which the scanning object currently is 0-359deg
object_angle =0
#matplotlib
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_xlim(-230, 230)
ax.set_ylim(-230, 230)
ax.set_zlim(-1,700)

img = cv2.imread('slika3.png')
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
text_output = open("Output_"+timestr+".asc", "w")

cv2.imshow('range',img2)

	
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
				break;
				
				#plt.pause(0.01)
				#time.sleep(0.01)
		position+=vertical_step
	plt.draw()
	plt.pause(0.01)
	print object_angle
	object_angle+=10
text_output.close()
#plt.show()	

cv2.imshow('range',img2)
cv2.imshow('org',img)
cv2.waitKey(0)
cv2.destroyAllWindows()