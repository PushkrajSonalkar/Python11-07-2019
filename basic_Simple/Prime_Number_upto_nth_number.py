# Prime number up to nth number

n = int(raw_input("Enter the number upto you want all prime numbers\n"))
print "\nThe Prime Number between 0 to %d :" % n

for val in range(2, n + 1):
    if val > 1:
        for n in range(2, val):
            if val % n == 0:
                break
        else:
            print val
