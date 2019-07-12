# Python code to demonstrate the working of
# fromlist() and tolist()

# importing "array" for array operations
import array

# initializing array 1 with array values
# initializes array with signed integers
arr1 = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print "Original array is: ",
for i in range(len(arr1)):
    print arr1[i],

print "\n"

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr1.fromlist(li)

# print modified array
print "Modified array: ",
for i in range(len(arr1)):
    print arr1[i],

print "\n"

# using tolist() to convert array into list
li2 = arr1.tolist()

# printing the new list
print "New created list is: ",
for i in range(len(li2)):
    print li2[i],
