# Python | Convert a list into tuple of lists

# Method #1 : Using Comprehension

# Python code to convert a list into tuple of lists

# Initialisation of list
Input = ['Arnav', 'Ravindra', 'Sonalkar']

# Using list Comprehension
Output = tuple([name] for name in Input)

# printing output
print Output
