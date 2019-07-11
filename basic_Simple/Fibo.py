# Fibonacci Series
from sys import stdout
print "Enter the Number"
number = int(raw_input("> "))
a = 0
b = 1

print("\nfibonacci series is:")
stdout.write("%d " % a)
stdout.write("%d " % b)
for i in range(2, number):
    c = a + b
    stdout.write("%d " % c)
    a = b
    b = c

