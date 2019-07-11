# File open File read
from sys import argv

script, filename = argv

txt = open(filename, "rb")

print "Here is your file %r" % filename
print txt.read()

