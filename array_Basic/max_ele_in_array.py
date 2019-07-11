# Maximum element in array


def max_ele(arr, n):
    maxi = arr[0]

    for i in range(1, n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi


num_array = []
n = int(raw_input("Enter the size of array\n"))
print "Enter the numbers in array"
for j in range(n):
    num = int(raw_input("> "))
    num_array.append(num)

print "Num array : ", num_array
n = len(num_array)
print "Maximum number in Array is %d " % max_ele(num_array, n)
