# Number
from sys import stdout
r = 10
for i in range(1, r):
    for j in range(1, i + 1):
        stdout.write("%d " % j)
    stdout.write("\n")
