# Array Reverse program

num_array = []
n = int(raw_input("Enter the size of array\n"))
print "Enter the numbers in array"
for i in range(n):
    num = int(raw_input("> "))
    num_array.append(num)

print "Num array : ", num_array
j = 0
length = len(num_array)
for i in range(length):
    print num_array[-1 + j]
    j -= 1
