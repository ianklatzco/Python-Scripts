from math import sqrt
from time import sleep

s = 0
a = 0
b = 0
c = 0
x = 0

s = input("Semiperimeter?")
a = input("A?")
b = input("B?")
c = input("C?")

x = s*(s-a)(s-b)(s-c)

answer = sqrt(x)

print answer
sleep(2)