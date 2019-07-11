# Dictionaries

# create a mapping of state to abbreviation
states = {
    'India': 'IN',
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
city = {'IN': 'Delhi', 'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville', 'NY': 'New York', 'OR': 'Portland'}

# print out some cities
print '-' * 10
print "IN State has: ", city['IN']
print "NY State has: ", city['NY']
print "OR State has: ", city['OR']

# print some states
print '- ' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '- ' * 10
print "Michigan has: ", city[states['Michigan']]
print "Florida has: ", city[states['Florida']]

# print every state abbreviation
print '- ' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '- ' * 10
for abbrev, cities in city.items():
    print "%s has the city %s" % (abbrev, cities)

# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, city[abbrev])

print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)
if not state:
    print "Sorry, No Texas."

# get a city with a default value
cities = city.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % cities
