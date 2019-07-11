# Simple Interest

p = raw_input("Enter Value of Principal\n")
p = float(p)

n = raw_input("Enter the Time period\n")
n = float(n)

r = raw_input("Enter the Rate\n")
r = float(r)

si = (p * n * r)/100

print "Simple Interest is %0.2f" % si
