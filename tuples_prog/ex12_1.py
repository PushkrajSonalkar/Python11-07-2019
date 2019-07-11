# Python | Dictionary to list of tuple conversion

# Method #1 : Using list comprehension + tuple + items()

# Dictionary to list of tuple conversion
# using list comprehension + tuple + items()

# initializing Dictionary
ini_dict = {'Arnav': (25, 'Sonalkar'), "Mauli": (26,"Kawade")}

# printing original dictionary
print "The original dictionary : ", ini_dict

# using list comprehension + tuple + items()
# Dictionary to list of tuple conversion
res = [(key, i, j) for key, (i, j) in ini_dict.items()]

# print result
print "After conversion: ", res
