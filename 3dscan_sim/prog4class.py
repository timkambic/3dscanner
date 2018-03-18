print "Running 3dscann \n importing ..."
import cv2
import numpy as np
import math
import time
import sys
from visual import display,arrow,rate,points,vector,color



class LiveDisplay:
	scalePoints = 0.3 #scale down all point so they fit display
	def __init__(self):
		# make window to display live data from scan
		scene2 = display(title='Live scan',x=0, y=0, width=600, height=400, background=(0.8,0.8,0.8),center=(0,0,100),forward=(-0.05,0.1,-1))
		# add coordinate axis
		arrow(pos=vector(0,0,0), axis=vector(100,0,0),color = color.red,shaftwidth=1)
		arrow(pos=vector(0,0,0), axis=vector(0,100,0),color = color.green,shaftwidth=1)
		arrow(pos=vector(0,0,0), axis=vector(0,0,300),color = color.blue,shaftwidth=1)
	def addPoint(self,x,y,z,r,g,b):
		point_pos = [(int(x)*self.scalePoints,int(y)*self.scalePoints,int(z)*self.scalePoints)]
		points(pos=point_pos, size=2, color=(r,g,b))
	

class Scan3d:
	#cam_laser_angle = 45
	#Sin45 = 0.70710678118
	multiplierAngle =1/ 0.70710678118
	# hold the value at which the scanning object currently is 0-359deg
	object_angle =0
	laser_low = np.array([0,0,0])  # lower end of laser color
	laser_high = np.array([180,255,247]) # higher end of laser color
	nSteps =201#67*4 # number of vertical steps (number of vertical points)  (more bit veckratnik visine drgac se zgodijo cudne stvari :/ :( )
	
	def __init__(self,angle):
		self.liveDisplay = LiveDisplay()
		timestr = time.strftime("%Y%m%d-%H%M%S")
		self.text_output = open("outputs/Output_"+timestr+".asc", "w") #Output file for coordinates of all points
		self.angle_to_rotate = angle
		# how many points to skip when displaying live 
		self.skipDrawingPoints = 3
		cv2.namedWindow('org',cv2.WINDOW_NORMAL)
		cv2.namedWindow('laser-line',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('org', 400,400)
		cv2.resizeWindow('laser-line',300,300)
		cv2.moveWindow('org', 600,0)
		cv2.moveWindow('laser-line',1010,0)
	def pixelsToCartesian3D(self,x,y):
		# convert from pixel position to polar coordinate system
		D = self.width/2 - x 
		r = D*self.multiplierAngle
		# polar to cartesian
		radians = math.radians(self.object_angle)
		xk = r * math.cos(radians)
		yk = r * math.sin(radians)
		zk = self.height-y
		return xk,yk,zk
	
	def turnOneStep(self):
		print ""
	
	def Scan(self):
		for fi in range(self.angle_to_rotate):
			#wait for turntable to rotate 1 step #DUMMY
			self.turnOneStep()
			#get image from webcam
			img = cv2.imread('slika2.png')
			img2 = img.copy()
			self.height, self.width = img.shape[:2]
			print "image size (h,w):",self.height, "x", self.width
			self.vertical_step = self.height/self.nSteps
			print "vertical step",self.vertical_step
			# draw line where the center of scan table should be
			cv2.line(img,(self.width/2-1,0),(self.width/2-1,self.height),(0,255,0),2) # draw center of the image
			img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV) # convert to hsv 
			# threshold laser out of the image
			img2 = cv2.inRange(img2, self.laser_low, self.laser_high) # find laser line
			img2 = cv2.bitwise_not(img2) # might not be necesarry
			#position = 0 # starting postion of vertical scann, starts at top
			drawPoint = self.skipDrawingPoints-1
			for i in range(self.nSteps):
				nOkPixels = 0
				for x in range(self.width):
					position = i*self.vertical_step
					if img2[position,x] > 0 and nOkPixels <1:
						cv2.circle(img,(x, position), 1, (255,0,0), -1)
						nOkPixels +=1
						xk,yk,zk = self.pixelsToCartesian3D(x,position)
						
						#FUNCTION TO TRANSLATE FROM 'pixel' UNITS TO METERS !!!
						#
						
						# write x,y,z to output file
						self.text_output.write(str(xk)+" "+str(yk)+" "+str(zk)+"\n")
						#print xk,yk,zk
						#dont draw all point due to RAM usage
						drawPoint+=1
						if drawPoint == self.skipDrawingPoints:
							rate(500)
							r=i/67.0
							g=fi/360.0
							b=fi/360.0
							self.liveDisplay.addPoint(xk,yk,zk,r,g,b)
							drawPoint=0
						break;
				#position+=self.vertical_step
				print "position: ",position
			cv2.imshow('laser-line',img2)
			cv2.imshow('org',img)
			#print self.object_angle
			self.object_angle+=1
			#cv2.waitKey(0)
	
	def exit(self):
		print "exiting"
		self.text_output.close()
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		
if __name__ == "__main__":
	scanner1 = Scan3d(360)
	scanner1.Scan()
	scanner1.exit()
