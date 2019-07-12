# Mathematical Functions in Python | Set 3 (Trigonometric and Angular Functions)
# Python code to demonstrate the working of
# sin() and cos()
# tan() and hypot()
# degrees() and radians()

# importing "math" for mathematical operations
import math

a = math.pi / 6
b = 3
c = 4
d = 30
print "Value of a is:", a

"""sin() :- This function returns the sine of value passed as argument. 
The value passed in this function should be in radians."""
# returning the value of sine of pi/6
print "The value of sine of pi/6 is : ", math.sin(a)

"""cos() :- This function returns the cosine of value passed as argument. 
The value passed in this function should be in radians."""
# returning the value of cosine of pi/6
print "The value of cosine of pi/6 is : ", math.cos(a)

"""tan() :- This function returns the tangent of value passed as argument.
The value passed in this function should be in radians."""
# returning the value of tangent of pi/6
print "The value of tangent of pi/6 is : ", math.tan(a)

"""hypot(a, b) :- This returns the hypotenuse of the values passed in arguments.
Numerically, it returns the value of sqrt(a*a + b*b)."""
# returning the value of hypotenuse of 3 and 4
print "The value of hypotenuse of 3 and 4 is : ", math.hypot(b, c)

"""degrees() :- This function is used to convert argument value from radians to degrees."""
# returning the converted value from radians to degrees
print "The converted value from radians to degrees is : ", math.degrees(a)

"""radians() :- This function is used to convert argument value from degrees to radians."""
# returning the converted value from degrees to radians
print "The converted value from degrees to radians is : ", math.radians(d)
