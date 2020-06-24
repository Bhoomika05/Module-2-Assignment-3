#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
r=float(input("enter the radius of the circle  "))
area=math.pi*r*r
print("area of the circle",area)


# In[7]:


from math import tan,pi
n = int(input("number of sides: "))
length = float(input("length of a side: "))
area = n * (length**2) / (4 * tan(pi / n))
print("The area of the polygon is: ",area)


# In[8]:


import math
def segmentarea(r,angle):
    sectorarea = pi * (r * r) * (angle / 360) 
    trianglearea = 1 / 2 *(r * r) *math.sin((angle * pi) / 180) 
  
    return sectorarea - trianglearea; 
r=int(input("enter the radius"))
angle=int(input("enter the angle"))
print("area of minor segment=",segmentarea(r,angle))
print("area of major segment=",segmentarea(r,(360-angle)))


# In[10]:


from random import shuffle
l1 = [100,1,2,3,30,40,"hai","hello"]
shuffle(l1)
print(l1)


# In[12]:


import random
n = random.randint(1,1000)
print(n)
while(n<1000):
    n=n+50
    print(n)


# In[14]:


import math
s=math.sin(60)
print(s)


# In[16]:


import math
c=math.cos(math.pi)
print(c)


# In[17]:


import math
t=math.tan(90)
print(t)


# In[18]:


import math

print(math.sin((0.86602540378443860009)))


# In[22]:


print(5**8)


# In[23]:


print(400**0.5)


# In[24]:


import math
print(5*(math.e))


# In[25]:


import math
print(math.log2(1024))


# In[26]:


import math
print(math.log10(1024))


# In[27]:


import math
print(math.floor(23.56))
print(math.ceil(23.56))

