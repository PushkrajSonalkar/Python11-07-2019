# Python code to demonstrate the working of
# pop() and remove()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print "Original array is: ",
for i in range(len(arr)):
    print arr[i],

print "\n"

# using pop() to remove element at 2nd position
print "Popped element is: ",
print arr.pop(2)

# Array after popping an element
print "Array after popping: ",
for i in range(len(arr)):
    print arr[i],
print "\n"

# using remove() to remove 1st occurrence of 1
arr.remove(1)

print "Array after remove(): ",
for i in range(len(arr)):
    print arr[i],

print "\n"