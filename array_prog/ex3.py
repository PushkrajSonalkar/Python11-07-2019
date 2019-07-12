# Python code to demonstrate the working of
# index() and reverse()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print "Original array is: ",
for i in range(len(arr)):
    print arr[i],

print "\n"

# using index() to print index of 1st occurrenece of 2
print "Index of 1st occurrence of 2 is: ",
print arr.index(2)

# using reverse() to reverse the array
arr.reverse()

# printing reversed array
print "Reversed array is: ",
for i in range(len(arr)):
    print arr[i],
