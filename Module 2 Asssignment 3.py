1.area of a circle


import math
r=float(input("enter the radius of the circle  "))
area=math.pi*r*r
print("area of the circle",area)


2.area of a regular polygon


from math import tan,pi
n = int(input("number of sides: "))
length = float(input("length of a side: "))
area = n * (length**2) / (4 * tan(pi / n))
print("The area of the polygon is: ",area)


3.area of a segment of a circle


import math
def segmentarea(r,angle):
    sectorarea = pi * (r * r) * (angle / 360) 
    trianglearea = 1 / 2 *(r * r) *math.sin((angle * pi) / 180) 
  
    return sectorarea - trianglearea; 
r=int(input("enter the radius"))
angle=int(input("enter the angle"))
print("area of minor segment=",segmentarea(r,angle))
print("area of major segment=",segmentarea(r,(360-angle)))

4.Shuffle lists

from random import shuffle
l1 = [100,1,2,3,30,40,"hai","hello"]
shuffle(l1)
print(l1)

5.random numbers generator

import random
n = random.randint(1,1000)
print(n)
while(n<1000):
    n=n+50
    print(n)
    
    
6.program using math module
I)


import math
s=math.sin(60)
print(s)


II)


import math
c=math.cos(math.pi)
print(c)


III)


import math
t=math.tan(90)
print(t)


IV)


import math

print(math.sin((0.86602540378443860009)))


V)


print(5**8)


VI)


print(400**0.5)


VII)


import math
print(5*(math.e))


VIII)


import math
print(math.log2(1024))


IX)


import math
print(math.log10(1024))


X)


import math
print(math.floor(23.56))
print(math.ceil(23.56))

