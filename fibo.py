import time
x = 1
y = 1
while x < 100:
	# time.sleep(.1)
	print x,y
	x = y + x
	# print x,y
	y = x - y
	print x,y
	print 