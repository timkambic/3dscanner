print "Running 3dscann \n importing opencv,numpy,math,time,sys,visual..."
import math
import time
import sys
import cv2
import numpy as np
import serial
from visual import display,arrow,rate,points,vector,color


class LiveDisplay:
	scalePoints = 0.3 #scale down all point so they fit display
	def __init__(self):
		# make window to display live data from scan
		self.scene2 = display(title='Live scan',x=0, y=0, width=600, height=400, background=(0.8,0.8,0.8),center=(0,0,100),forward=(-0.05,0.1,-1))
		# add coordinate axis
		arrow(pos=vector(0,0,0), axis=vector(100,0,0),color = color.red,shaftwidth=1)
		arrow(pos=vector(0,0,0), axis=vector(0,100,0),color = color.green,shaftwidth=1)
		arrow(pos=vector(0,0,0), axis=vector(0,0,300),color = color.blue,shaftwidth=1)
	def addPoint(self,x,y,z,r,g,b):
		point_pos = [(int(x)*self.scalePoints,int(y)*self.scalePoints,int(z)*self.scalePoints)]
		points(pos=point_pos, size=2, color=(r,g,b))
	def Close(self):
		self.scene2.delete()
		
class Scan3d:
	#angle between center of camera and laser
	cam_laser_angle = math.pi/4
	# hold the value at which the scanning object currently is 0-359deg
	object_angle =0
	laser_low = 51  # lower end of laser color
	laser_high = 255 # higher end of laser color
	nSteps_vertical =240#240#67*4 # number of vertical steps (number of vertical points)  (more bit veckratnik visine drgac se zgodijo cudne stvari :/ :( )
	deg_per_step = 360.0 / 372.0
	#deg_per_step = 360.0 / (372.0 * 2)
	#where on the image to start and stop looking for laser
	limit_up = 0
	limit_down = 720
	# how many points to skip when displaying live 
	skipDrawingPoints = 3
	
	def __init__(self,angle):
		
		timestr = time.strftime("%Y%m%d-%H%M%S")
		self.text_output = open("outputs/Output_"+timestr+".asc", "w") #Output file for coordinates of all points
		self.text_output.write("0 0 0 \n")
		
		self.openscad_doc = open("doc_openscad3.scad","w")
		
		self.rotate_steps = int(angle /self.deg_per_step) #for 360 deg stepper must turn 372 'steps' (11 steps per 'step')
		
		# open serial link to arduino for controling stepper motor
		self.serial1 = serial.Serial('COM9',9600,timeout = 5)
		
		self.cap = cv2.VideoCapture(1)
		
		print "Rotate steps: ", self.rotate_steps
		print "Vertical steps: ", self.nSteps_vertical
		print "degrees per step: ", self.deg_per_step
		print "--"
		
	def options(self):
		cv2.namedWindow('settings',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('settings', 400,400)
		cv2.namedWindow('live',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('live', 400,400)
		
		cv2.createTrackbar('brightness','settings',50,255,nothing)
		cv2.createTrackbar('limit UP','settings',10,500,nothing)
		cv2.createTrackbar('limit DOWN','settings',10,500,nothing)
		
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
		while True:
			brightness_val = cv2.getTrackbarPos('brightness','settings')
			self.cap.set(cv2.CAP_PROP_BRIGHTNESS,brightness_val)
			
			img_prev = self.cap.read()[1]
			
			self.limit_up = cv2.getTrackbarPos('limit UP','settings')
			cv2.line(img_prev,(0,self.limit_up),(1280,self.limit_up),(0,255,0),2)
			self.limit_down = cv2.getTrackbarPos('limit DOWN','settings')
			cv2.line(img_prev,(0,720-self.limit_down),(1280,720-self.limit_down),(255,0,0),2)
			
			cv2.imshow('live',img_prev)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		cv2.destroyWindow('live')
		cv2.destroyWindow('settings')
		
	def pixelsToCartesian3D(self,x,y):
		# convert from pixel position to polar coordinate system
		D = self.width/2 - x 
		r = D*math.sin(self.cam_laser_angle) #self.multiplierAngle
		# polar to cartesian
		radians = math.radians(self.object_angle)
		xk = r * math.cos(radians)
		yk = r * math.sin(radians)
		zk = self.height-y
		return xk,yk,zk
	
	def addOPENSCAD(self,img_x,img_y):
		D = self.width/2 - img_x
		r = D*math.sin(self.cam_laser_angle)
		z = self.height-img_y
		str_r = "%.3f" % r
		str_z = "%.3f" % z
		self.openscad_doc.write(" [" +str_r+ "," +str_z+ "], ")

	def Scan(self):
		 
		#time.sleep(1) # wait to make sure serial1 is initialized 
		print "\nserial1 port is open?:",self.serial1.isOpen()
		self.liveDisplay = LiveDisplay()
		cv2.namedWindow('org',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('org', 400,400)
		cv2.moveWindow('org', 600,0)
		cv2.namedWindow('laser-line',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('laser-line',400,400)
		cv2.moveWindow('laser-line',1010,0)
		
		for fi in range(self.rotate_steps):
			#wait for turntable to rotate 1 step 
			self.serial1.write("k")
			response = self.serial1.read()
			if response == "": 
				print "no data response after 5s , timeout reached"
			print  self.object_angle, "  ", fi, "  ", response
			
			#get image from webcam
			#taking two images because it doesnt work with one ???!!??
			img = self.cap.read()[1]
			img = self.cap.read()[1]
			img2 = img.copy() # copy for working
			self.height, self.width = img.shape[:2]
			#print "image size (h,w):",self.height, "x", self.width
			self.vertical_step = int(  float(self.height )  / self.nSteps_vertical)
			#print "vertical step",self.vertical_step
			# draw line where the center of scan table should be
			cv2.line(img,(self.width/2-1,0),(self.width/2-1,self.height),(0,255,0),2) # draw center of the image
			# get the R channel
			img2 = img2[:,:,2]
			# threshold laser out of the image
			img2 = cv2.inRange(img2, self.laser_low, self.laser_high) # find laser line
			# EDIT IMAGE
			#
			
			drawPoint = self.skipDrawingPoints-1
			
			self.openscad_doc.write("rotate([90,0,"+str(self.object_angle)+"])linear_extrude(height=2, center=false, convexity=14, twist=0) polygon([")
			#self.openscad_doc.write("rotate([90,0,"+str(self.object_angle)+"])rotate_extrude(angle = 1, convexity = 14) polygon([")
			
			
			for i in range(self.limit_up, (self.height-self.limit_down), self.vertical_step):
				position_vertical = i		
				#print position_vertical
				# find the center pixel of line
				first = 1
				start = 0
				end = 0
				for x in range(self.width-10):
					if img2[position_vertical,x] > 0 :
						if first==1:
							start = x
							first = 0
						if img2[position_vertical,x+1] ==0:
							end = x
							break
				
				if start !=0 and end !=0:
					#print "adding point"
					x_center = int(start+(end-start)/2.0)	
					cv2.circle(img,(x_center, position_vertical), 1, (255,255,0), -1)	
					xk,yk,zk = self.pixelsToCartesian3D(x_center,position_vertical)		
					self.addOPENSCAD(x_center,position_vertical)
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
			
			self.openscad_doc.write("]);  \n \n")		
			cv2.line(img,(0,self.limit_up),(1280,self.limit_up),(0,255,0),2)
			cv2.line(img,(0,720-self.limit_down),(1280,720-self.limit_down),(255,0,0),2)
			cv2.imshow('laser-line',img2)
			cv2.imshow('org',img)
			cv2.waitKey(1)
			
			self.object_angle+= self.deg_per_step
			
		print "DONE"
		print "\a \a"
		
	def Exit(self):
		print "exiting"
		self.text_output.close()
		self.openscad_doc.close()
		self.serial1.write('s') # turn off the motor
		#self.serial1.__del__()
		self.serial1.close()
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		self.liveDisplay.Close()
		
def nothing(x):
	pass
	
if __name__ == "__main__":
	scanner = Scan3d(360)
	scanner.options()
	scanner.Scan()
	scanner.Exit()
	
	# try: 
		# scanner.Scan()	
	# except KeyboardInterrupt:
		# scanner.Exit()
	# #sys.exit(0)
	