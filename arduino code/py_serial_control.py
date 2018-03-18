import serial
import time
#initialize serial
serial = serial.Serial('COM9',9600,timeout = 5) 
time.sleep(3) # wait to make sure serial is initialized 
print "\nSerial port is open?:",serial.isOpen()

# serial.write("k")
# time.sleep(3)
# response = serial.read()
# if response == "": 
	# print "no data response after 5s , timeout reached"
# print 0, " ", response
#time.sleep(1)

for i in range(0,372):
	serial.write("k")
	response = serial.read()
	if response == "": 
		print "no data response after 5s , timeout reached"
	print i, " ", response
serial.write('s') # turn off the motor
time.sleep(120)

serial.close()