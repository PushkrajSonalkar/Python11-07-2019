# sum of array elements

num_array = []
sum = 0
n = int(raw_input("Enter the size of array\n"))
print "Enter the numbers in array"
for i in range(n):
    num = int(raw_input("> "))
    num_array.append(num)

print "Num array : ", num_array

for i in range(n):
    sum += num_array[i]

print "sum of elements in array is ", sum
