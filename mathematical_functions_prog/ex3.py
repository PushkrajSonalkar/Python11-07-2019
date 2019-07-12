# Python code to demonstrate the working of
# copysign() and gcd()

# importing "math" for mathematical operations
import math

a = -10
b = 5.5
c = 15
d = 5

"""copysign(a, b) :- This function returns the number with the
 value of 'a' but with the sign of 'b'. 
The returned value is float type."""

# returning the copysigned value.
print "The copysigned value of %d and %0.1f is : %0.1f" % (a, b, math.copysign(b, a))

""" gcd() :- This function is used to compute the greatest common divisor of
 2 numbers mentioned in its arguments.
This function works in python 3.5 and above."""

# returning the gcd of 15 and 5
# print "The gcd of %d and %d is %d" % (d, c, math.gcd(d, c))
print "math.gcd() is present in python 3.5 and above"
