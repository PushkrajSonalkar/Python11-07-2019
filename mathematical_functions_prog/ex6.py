# Mathematical Functions in Python | Set 4 (Special Functions and Constants)
# Python code to demonstrate the working of
# gamma()
# const. pi and e
# inf, nan, isinf(), isnan()

# importing "math" for mathematical operations
import math

a = 4

"""gamma() :- This function is used to return the gamma function of the argument."""
# returning the gamma() of 4
print "The gamma() of 4 is : ", math.gamma(a)

""" pi :- This is an inbuilt constant that outputs the value of pi(3.141592)."""
# returning the value of const. pi
print "The value of const. pi is : ", math.pi

""" e :- This is an inbuilt constant that outputs the value of e(2.718281)."""
# returning the value of const. e
print "The value of const. e is : ", math.e

"""
nan :- This constant denotes "Not a number" in python. 
This constant is defined in python 3.5 and above.
isnan() :- This function returns true if the number is "nan" else returns false.
# checking if number is nan
if math.isnan(math.nan):
    print "The number is nan ", math.nan
else:
    print "The number is not nan"
"""

"""inf :- This is a positive floating point infinity constant. 
-inf is used to denote the negative floating point infinity. 
This constant is defined in python 3.5 and above.
isinf() :- This function is used to check whether the value is an infinity or not.

# checking if number is positive infinity
if math.isinf(math.inf):
    print "The number is positive infinity "
else:
    print "The number is not positive infinity"
"""