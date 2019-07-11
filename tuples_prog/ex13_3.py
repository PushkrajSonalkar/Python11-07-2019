# Python | Convert a list into tuple of lists

# Method #3 : Using Map + zip

# Python code to convert a list into tuple of lists

# Initialisation of list
Input = ['Arnav', 'Ravindra', 'Sonalkar']

# Using list Comprehension
Output = tuple(map(list, zip(Input)))

# printing output
print Output
