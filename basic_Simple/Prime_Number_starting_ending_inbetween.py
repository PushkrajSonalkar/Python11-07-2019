# Prime number Prime_Number_starting_ending_in between

n = int(raw_input("Enter the starting numbers\n"))
l = int(raw_input("Enter the starting numbers\n"))
print "\nThe Prime Number between %d to %d :" % (n, l)

for val in range(n, l + 1):
    if val > 1:
        for n in range(2, val):
            if val % n == 0:
                break
        else:
            print val
