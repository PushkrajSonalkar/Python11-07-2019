# Minimum element in array


def min_ele(arr, z):
    mini = arr[0]

    for i in range(1, z):
        if arr[i] < mini:
            mini = arr[i]
    return mini


num_array = []
n = int(raw_input("Enter the size of array\n"))
print "Enter the numbers in array"
for j in range(n):
    num = int(raw_input("> "))
    num_array.append(num)

print "Num array : ", num_array
n = len(num_array)
print "Minimum number in Array is %d " % min_ele(num_array, n)
