# Adding elements to a Dictionary and Accessing elements from a Dictionary

# Creating an empty Dictionary
Dict = {}
print "Empty Dict: ", Dict

# Adding elements one at a time
Dict[0] = 'Arnav'
Dict[1] = 'Sonalkar'
Dict[2] = 25

print "Dict after adding 3 elements: ", Dict

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print "Dict after adding 3 elements: ", Dict

# Updating existing Key's Value
Dict[2] = 'Welcome'
print "After updating Dict: ", Dict

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Goes'}}
print "After adding Nested key Dict: ", Dict

# accessing a element using key
print "\nAccessing a Element using key: ", Dict['Value_set']

# accessing a element using key
print "\nAccessing a Element using key: ", Dict[1]

# accessing a element using get()
# method
print "Accessing a element using get: ", Dict.get(0)
