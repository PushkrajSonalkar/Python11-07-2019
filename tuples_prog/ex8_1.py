# Python | Reversing a Tuple

# Method 1: Using the slicing technique.


def reverse(tuples):
    new = tuples[::-1]
    return new


# Driver Code
Tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Before Reversing Tuple
print Tuple1

# After Reversing Tuple
print reverse(Tuple1)
