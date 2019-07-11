#  even length words in a string


def print_words_even(s):

    s = s.split(' ')

    for word in s:

        if len(word) % 2 == 0:
            print(word)


def print_words_odd(s):

    s = s.split(' ')

    for word in s:
        if len(word) % 2 != 0:
            print (word)


z = raw_input("Enter string\n")
print "Select whether you want to get odd length word or even 1. Odd 2. Even \n Enter 1 or 2 as per choice"
ch = int(raw_input("> "))
if ch == 1:
    print_words_odd(z)
elif ch == 2:
    print_words_even(z)
else:
    print "Enter valid choice"
