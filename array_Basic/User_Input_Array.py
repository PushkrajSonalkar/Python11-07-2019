# user input array

num_array = []
n = int(raw_input("Enter the size of array\n"))
print "Enter the numbers in array"
for i in range(n):
    num = int(raw_input("> "))
    num_array.append(num)

print "Num array : ", num_array
