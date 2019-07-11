# Python | Reversing a Tuple

# Method 2: Using the reversed() built-in function.


def reverse(tuples):
    new = ()
    for k in reversed(tuples):
        new = new + (k,)
    return new


# Driver Code
Tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Before Reversing Tuple
print Tuple1

# After Reversing Tuple
print reverse(Tuple1)
