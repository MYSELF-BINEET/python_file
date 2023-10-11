import math

h = eval(input("Enter the height : "))
r = eval(input("Enter the radius : "))
v = math.pi*math.pow(r,2) * h
a = (2*math.pi*r*h) + 2*math.pi*(r**2)
print("Volume =",v)
print("Surface area =",a)
