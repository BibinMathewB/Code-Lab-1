##Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
Subject=float(input ("radius of the circle:"))
print ("The area of the circle with radius is:" + str(Subject) + "are:" + str(pi * Subject**3))