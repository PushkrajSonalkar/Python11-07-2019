# Python | Convert a list into tuple of lists

# Method #2 : Using Map + Lambda

# Python code to convert a list into tuple of lists

# Initialisation of list
Input = ['Arnav', 'Ravindra', 'Sonalkar']

# Using list Comprehension
Output = tuple(map(lambda x: [x], Input))

# printing output
print Output
