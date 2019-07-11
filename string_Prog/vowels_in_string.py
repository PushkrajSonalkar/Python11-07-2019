# find number of vowels in string


def vowel_count(str1):
    c = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str1:
        if alphabet in vowel:
            c += 1
    print "No. of Vowels :", c


z = raw_input("Enter string\n")
vowel_count(z)
