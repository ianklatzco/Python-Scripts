import time
x = 0
fizz = x+1
buzz = x/5

while x < 100:
	time.sleep(1)
	x = x+1
	print x
	if fizz != 0:
		print fizz