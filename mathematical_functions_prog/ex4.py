# Mathematical Functions in Python | Set 2 (Logarithmic and Power Functions)
# Python code to demonstrate the working of
# exp() and log()
# log2() and log10()
# pow() and sqrt()

# importing "math" for mathematical operations
import math

"""exp(a) :- This function returns the value of e raised to the power a (e**a)"""

# returning the exp of 4
print "The e**4 value is : ", math.exp(4)

"""log(a, b) :- This function returns the logarithmic value of a with base b.
If base is not mentioned, the computed value is of natural log."""

# returning the log of 2,3
print "The value of log 2 with base 3 is : ", math.log(2, 3)

"""log2(a) :- This function computes value of log a with base 2. 
This value is more accurate than the value of the function discussed above.
"""
# returning the log2 of 16
# print "The value of log2 of 16 is : ", math.log2(16)

print "math.log2(X) is not present in python 2.7"

"""log10(a) :- This function computes value of log a with base 10. 
This value is more accurate than the value of the function discussed above."""

# returning the log10 of 10000
print "The value of log10 of 10000 is : ", math.log10(10000)

""" pow(a, b) :- This function is used to compute value of a raised to the power b (a**b)."""
# returning the value of 3**2
print "The value of 3 to the power 2 is : ", math.pow(3, 2)

""" sqrt() :- This function returns the square root of the number."""
# returning the square root of 25
print "The value of square root of 25 : ", math.sqrt(25)
