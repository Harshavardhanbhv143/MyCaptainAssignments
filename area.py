from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius 1.1 is: " + str(pi * r**2))



for file name:
  filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
