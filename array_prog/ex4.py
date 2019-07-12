# Array in Python | Set 2 (Important Functions)

# Python code to demonstrate the working of
# typecode(), itemsize(), buffer_info()

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

# using typecode to print datatype of array
print "The datatype of array is: ",
print arr.typecode

# using itemsize to print itemsize of array
print "The itemsize of array is: ",
print arr.itemsize

# using buffer_info() to print buffer info. of array
print "The buffer info of array is: ",
print arr.buffer_info()
