from visual import *
import random
import time
arrow(pos=vector(0,0,0), axis=vector(1,0,0),color = color.red)
arrow(pos=vector(0,0,0), axis=vector(0,1,0),color = color.green)
arrow(pos=vector(0,0,0), axis=vector(0,0,1),color = color.blue)

#sphere(pos = vector(-1,0,0), radius=0.5, color = color.green)
points_pos = [(1,1,1),(2,2,2),(3,3,3),(3,4,3),(4,5,4)]

points(pos=points_pos, size=2, color=color.red)
xk=321
yk=312
zk=123
points(pos=[(xk,yk,zk)] , size=2, color=color.red)
xk=321
yk=312
zk=123
points(pos=[(xk,yk,zk)] , size=2, color=color.red)
xk=1
yk=1
zk=1
points(pos=[(xk,yk,zk)] , size=2, color=color.red)
while 1:
	#rate(50)
	time.sleep(0.02)
	xk+=1
	yk+=1
	zk+=1
	points(pos=[(xk,yk,zk)] , size=2, color=color.red)
