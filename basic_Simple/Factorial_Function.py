# Factorial using function i.e. recursion


def print_fact(num):
    if num == 1:
        return num
    else:
        return (num * print_fact(num - 1))


n = int(raw_input("Enter the number \n"))

if n < 0:
    print "Can\'t calculate factorial of negative number"
elif n == 0:
    print "Factorial of 0 is 1"
else:
    print "Factorial of %d is %d" %(n, print_fact(n))
