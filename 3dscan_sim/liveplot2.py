import matplotlib.pyplot as plt
import numpy
import time
hl, = plt.plot([], [])

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()
	
while True:
	time.sleep(0.1)
	point = numpy.random.normal(0, 1, 2)
	update_line(hl, 1)
	