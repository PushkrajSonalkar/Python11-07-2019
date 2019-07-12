# Array in Python | Set 1 (Introduction and Functions)

# Python code to demonstrate the working of
# array(), append(), insert()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print "New created array is: ",
for i in range(0, 3):
    print arr[i],

print "\n"
# using append() to insert new value at end
arr.append(4)
print "Appended Array: ",
# printing appended array
for i in range(0, 4):
    print arr[i],
print "\n"

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)
print "Array after insert 5 at 2nd position:",
for i in range(0, 4):
    print arr[i],
print "\n"
