# Star
from sys import stdout
r = 6
for k in range(r, 0, -1):
    for l in range(0, k - 1):
        stdout.write("* ")
    stdout.write("\n")
