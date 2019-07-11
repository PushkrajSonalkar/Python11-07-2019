# Read from one file and write to other file
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# Open file and save data into variable
in_file = open(from_file)
in_data = in_file.read()

print "Length of file in %d bytes" % len(in_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-Z to abort."

raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, All done"

out_file.close()
in_file.close()
