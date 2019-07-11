# Factorial Program

fact = 1

n = int(raw_input("Enter a number:\n"))
a = n

while n > 0:
    fact = fact * n
    n = n - 1

print "Factorial of %d is %d " % (a, fact)
