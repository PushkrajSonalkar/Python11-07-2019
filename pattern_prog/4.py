# Number
from sys import stdout
r = 10
for i in range(r):
    for j in range(i):
        stdout.write("%d "% i)
    stdout.write("\n")
