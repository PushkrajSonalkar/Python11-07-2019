# Creating a Dictionary and Nesting of it

# Creating an empty Dictionary
Dict = {}
print "Empty Dict: ", Dict

# Creating a Dictionary
# with Integer Keys
Dict1 = {1: 'Arnav', 2: 'Ravindra', 3: 'Sonalkar'}
print "Dict with int keys: ", Dict1

# Creating a Dictionary
# with Mixed keys
Dict2 = {'Name': 'Arnav', 1: [1, 2, 3, 4]}
print "Dict with mixed keys: ", Dict2

# Creating a Dictionary
# with dict() method
Dict3 = dict({1: 'Arnav', 2: 'Sonalkar'})
print "Dict with dict(): ", Dict3

# Creating a Dictionary
# with each item as a Pair
Dict4 = dict([(1, 'Arnav'), (2, 'Sonlkar')])
print "Dict with each item as pair: ", Dict4

# Creating a Nested Dictionary
# as shown in the below image
Dict5 = {1: 'Arnav', 2: 'Sonalkar', 3:{'A': 'Welcome', 'B': 'To', 'C': 'Centelon'}}
print "\nNasted Dict :", Dict5

# copy()
Dict6 = Dict1.copy()
print "Copied Dict: ", Dict6

# dictionary_name.values()
print Dict6.values()

# str()
print str(Dict6)

# keys()
print Dict6.keys()

# items()
print Dict6.items()

# has_key()
print Dict6.has_key(3)

# cmp()
print cmp(Dict1, Dict3)

# type()
print type(Dict)
