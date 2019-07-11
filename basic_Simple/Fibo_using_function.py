# Fibonacci with function
from sys import stdout


def print_fi(num):
    if num <= 1:
        return num
    else:
        return ( print_fi(num-1) + print_fi(num-2) )


n = int(raw_input("> "))
n = int(n)
if n <= 0:
    print "Please Enter Positive Integer"
else:
    print ("Fibonacci Series")
    for i in range(n):
        stdout.write("%d " % print_fi(i))
