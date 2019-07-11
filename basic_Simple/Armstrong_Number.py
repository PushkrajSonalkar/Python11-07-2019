# Armstrong Number


def power(n, r):
    c = 1
    p = 1
    for c in range(r):
        p *= n
    return p


num = raw_input("Enter a number\n")
num = int(num)

sum_ = 0
temp = 0
remainder = 0
digits = 0

temp = num

# Count Digits

while temp != 0:
    digits += 1
    temp /= 10

temp = num

while temp != 0:
    remainder = temp % 10
    sum_ = sum_ + power(remainder, digits)
    temp /= 10

if num == sum_:
    print "%d is Armstrong Number" % num
else:
    print "%d is not Armstrong Number" % num
