# Number 
from sys import stdout

r = 10
for i in range(1, r):
    for j in range(i, 0, -1):
        stdout.write("%d " % j)
    stdout.write("\n")


