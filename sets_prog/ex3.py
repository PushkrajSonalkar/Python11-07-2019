# Removing elements from the Set

# Addition of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print "Initial Set: ", set1

# Removing elements from Set
# using Remove() method
set1.remove(7)
set1.remove(11)
print "\nSet Elements after removing two elements: ", set1

# Removing elements from Set
# using Discard() method
set1.discard(8)
set1.discard(9)
print "\nSet Elements after removing two elements using discard(): ", set1

# Removing elements from Set
# using iterator method
for i in range(1, 5):
    set1.remove(i)

print "\nSet Elements after removing elements using iterator: ", set1

# Removing element from the
# Set using the pop() method
set1.pop()
print "\nSet Elements after removing elements using pop(): ", set1

# Removing all the elements from
# Set using clear() method
set1.clear()
print "\nSet Elements after clear(): ", set1
