# Removing Elements from Dictionary

# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print "Initial Dict: ", Dict

# Deleting a Key value
del Dict[6]
print "After Deleting a Specific key: ", Dict

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print "Deleting a key from Nested Dictionary: ", Dict

# Deleting a Key
# using pop()
Dict.pop(5)
print "Popping specific elements: ", Dict

# Deleting a Key
# using popitem()
Dict.popitem()
print "Pops 1st elements: ", Dict

# Deleting entire Dictionary
Dict.clear()
print "Deleting Entire Dict: ", Dict

