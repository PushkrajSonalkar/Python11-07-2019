# Star
from sys import stdout
r = 5
for i in range(0, r):
    for j in range(0, i+1):
        stdout.write("* ")
    stdout.write("\n")
for k in range(r, 0, -1):
    for l in range(0, k - 1):
        stdout.write("* ")
    stdout.write("\n")
