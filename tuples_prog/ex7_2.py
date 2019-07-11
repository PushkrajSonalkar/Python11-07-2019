# Python | Remove empty tuples from a list

# Method 2: Using the filter() method


def remove(tuples):
    tuples = filter(None, tuples)
    return tuples


# Driver Code
Tuple1 = [(), ('Arnav', 'Pranav', 1), (), ('Abhi', 'Atharva', 2), ('', ''), ('Viru', 'Mannu', 3), ()]

# Before Removing empty Tuples
print Tuple1

# After removing Tuples
print remove(Tuple1)
