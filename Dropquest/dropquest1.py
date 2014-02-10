import random
import time

foo = 0

v1 = 3
v2 = 8
v3 = 0
v4 = 0
v5 = 0
total = v1 + v2 + v3 + v4 + v5

#the v*correct is not related, just a placeholder to prevent the 1 from reading an an int
v1correct = 0
v2correct = 0
v3correct = 0
v4correct = 0
v5correct = 0
v6correct = 0

while foo != 1:
	v1 = random.randint(1,9)
	v2 = random.randint(1,9)
	v3 = random.randint(1,9)
	v4 = random.randint(1,9)
	v5 = random.randint(1,9)
	
	total = v1 + v2 + v3 + v4 + v5
	
	v1correct = v1 * v2 == 24
	v2correct = .5 * v2 == v4
	v3correct = v4 + v5 == v1 + v3
	v4correct = (total == 26)
	v5correct = v2 > v5
	
	print
	print v1, v2, v3, v4, v5
	print
	print v1correct, v2correct, v3correct, v4correct, v5correct
	# time.sleep(.1)
	
	if v1correct == True and v2correct == True and v3correct == True and v4correct == True and v5correct == True:
		print
		print "Victory!"
		print
		print v1
		print v2
		print v3
		print v4
		print v5
		foo = 1