#area of circle using math function 

import math 
r=int(input("enter radius"))
area=math.pi*(r*r)
print("area of circle",r,"is",area)



#area of regular polygon 

a=int(input("enter the length of the tangent between the center to any side"))
n=int(input("no of sides in polygon"))
s=int(input("enter the length of the side"))
area=(n*s*a)/2
print("area of regular polygon is",area)



#random number between 1 to 1000

import random
x=random.randrange(0,1000)
print("random numbers between 1 to 1000:",x)



#math module

x=math.sin(60)
print("sin 60=",x)
x=math.cos(math.pi)
print("cos(pi)=",x)
x=math.tan(90)
print("tan 90=",x)
x=math.sqrt(400)
print("aquare root of 400:",x)
x=math.floor(23.56)
print("floor=",x)
x=math.ceil(23.56)
print("ceil=",x)