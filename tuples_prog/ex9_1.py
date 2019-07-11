# Python | Split tuple into groups of n

# Method #1: Using enumerate and range function

# Python code to demonstrate
# how to split tuple
# into the group of k-tuples

# initialising tuple
ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,
             67, 45, 1, 1, 43, 65, 9, 10)

# Printing initial tuple
print "Initial Tuple :", ini_tuple

# code to group
# tuple into size 4 tuples
res = tuple(ini_tuple[x:x + 4]
            for x in range(0, len(ini_tuple), 4))

# Printing result
print "Resultant tuples: ", res
