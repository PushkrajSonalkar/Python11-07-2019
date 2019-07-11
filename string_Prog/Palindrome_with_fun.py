# Palindrome with function


def reverse(s):                 # function which return reverse of a string
    return s[::-1]


def is_palindrome(n):
    rev = reverse(n)
    if n == rev:
        return True
    return False


string = raw_input("Enter String\n")

if is_palindrome(string):
    print "String %s is Palindrome" % string
else:
    print "String %s is not Palindrome" % string
