# Python | Dictionary to list of tuple conversion

# Method #2 : Using list comprehension + items() + " + " operator

# Dictionary to list of tuple conversion
# using list comprehension + items() + "+" operator

# initializing Dictionary
ini_dict = {'Arnav': (25, 'Sonalkar'), "Mauli": (26,"Kawade")}

# printing original dictionary
print "The original dictionary : ", ini_dict

# using list comprehension + items() + "+" operator
# Dictionary to list of tuple conversion
res = [(key, ) + val for key, val in ini_dict.items()]

# print result
print "After conversion: ", res
