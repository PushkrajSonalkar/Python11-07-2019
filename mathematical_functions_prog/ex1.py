# Python code to demonstrate the working of
# ceil() and floor()

# importing "math" for mathematical operations
import math

a = 2.3

""" ceil() :- This function returns the smallest integral value greater than the number.
 If number is already integer, 
 same number is returned. """

# returning the ceil of 2.3
print "The ceil of %0.1f is %d " % (a, math.ceil(a))

"""  floor() :- This function returns the greatest integral value smaller than the number. 
If number is already integer, 
same number is returned.
"""

# returning the floor of 2.3
print "The floor of %0.1f is %d " % (a, math.floor(a))
