#  Adding Elements to a Set

# Creating a Set
set1 = set()
print "Initial blank set\n", set1

# Adding Elements to set
set1.add(8)
set1.add(5)
set1.add(78)
set1.add(15)
print "\nAfter adding elements set:", set1

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)

print "\nAfter adding elements using Iterator to set:", set1

# Adding Tuples to the Set
set1.add((6, 7))
print "\nAfter adding elements using Tuple to set:", set1

# Addition of elements to the Set
# using Update function
set1.union([10, 11])
print "\nAfter adding elements using update() to set:", set1
