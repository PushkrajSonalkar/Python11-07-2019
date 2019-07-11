# Tuple Creating

# Python program to demonstrate
# Addition of elements in a Set

# Creating an empty tuple

Tuple1 = ()
print "Initial Empty Tuple: "
print Tuple1

# Creating a Tuple with
# the use of Strings

Tuple2 = ('Arnav', 'Sonalkar')
print("\nTuple with the use of String: ")
print Tuple2

# Creating a Tuple with
# the use of list

list1 = [1, 2, 3, 4, 5]
print "\nTuple using List:"
print tuple(list1)

# Creating a Tuple
# with the use of loop
Tuple3 = ('Arnav')
n = 5
print "\nTuple with loop:"
for i in range(int(n)):
    Tuple3 = (Tuple3,)
    print Tuple3

# Creating a Tuple with the
# use of built-in function
Tuple4 = tuple('Arnav')
print "\nTuple with use of built-in function:"
print Tuple4

# Creating a Tuple with
# Mixed data types
Tuple5 = (1, 'Arnav', 2, 'Sonalkar')
print "\nTuple with mixed datatypes:"
print Tuple5

# Creating a Tuple
# with nested tuples
Tuple6 = (0, 1, 2, 3, 4, 5)
Tuple7 = ('Arnav', 'Sonalkar')
Tuple8 = (Tuple6, Tuple7)
print "\nTuple with nastes Tuples:"
print Tuple8

# Creating a Tuple
# with repetition
Tuple9 = ('Arnav',) * 3
print("\nTuple with repetition: ")
print(Tuple9)
