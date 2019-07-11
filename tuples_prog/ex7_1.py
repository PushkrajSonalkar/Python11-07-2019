# Python | Remove empty tuples from a list

# Method 1: Using the concept of List Comprehension


def remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


# Driver Code
Tuple1 = [(), ('Arnav', 'Pranav', 1), (), ('Abhi', 'Atharva', 2), ('', ''), ('Viru', 'Mannu', 3), ()]

# Before Removing empty Tuples
print Tuple1

# After removing Tuples
print remove(Tuple1)
