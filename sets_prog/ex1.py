# creating a set

# Python program to demonstrate
# Creation of Set in Python

# Creating a Set
set1 = set()
print "Initial blank set\n", set1

# Creating a Set with
# the use of a String
set2 = set("Arnav")
print "\nSet with use of String:", set2

# Creating a Set with
# the use of a List
set3 = set(["Arnav", "Ravindra", "Sonalkar"])
print "\nSet with use of List: ", set3

# Creating a Set with
# a List of Numbers
# (Having duplicate values)
set4 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print "\nSet with use of List of Numbers: ", set4

# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set5 = set([1, 2, "Arnav", 4, "Ravindra", 5, "Sonalkar"])
print "\nSet with use of mixed vales: ", set5

# Copy a set
set6 = set2.copy()
print "\nCopied Set: ", set6

# issubset()
print set2.issubset(set6)

# issuperset
print set2.intersection(set6)

# max
print max(set4)

# min
print min(set4)



