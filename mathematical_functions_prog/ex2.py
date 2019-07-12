# Python code to demonstrate the working of
# fabs() and factorial()

# importing "math" for mathematical operations
import math

a = - 10

b = 5

"""fabs() :- This function returns the absolute value of the number."""

# returning the absolute value.
print "The absolute value of %d is %0.1f " % (a, math.fabs(a))

"""factorial() :- This function returns the factorial of the number.
 An error message is displayed if number is not integral."""

# returning the factorial of 5
print "The factorial of %d is %d" %(b, math.factorial(b))
