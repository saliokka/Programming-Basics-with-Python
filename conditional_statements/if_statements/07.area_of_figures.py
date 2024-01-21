import math
from math import pi

shape = input()
sum = 0
if shape == "square":
    a = float(input())
    sum = a*a
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    sum = a*b
elif shape == "circle":
    r = float(input())
    sum = pi*(r**2)
elif shape == "triangle":
    a = float(input())
    b = float(input())
    sum = 1/2*a*b
print(f"{sum:.3f}")
