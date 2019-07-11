# While-Loops
i = 0
numbers = []
j = 10
while i < j:
    print "At the top is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d " % i

print "The numbers: "

for num in numbers:
    print num
