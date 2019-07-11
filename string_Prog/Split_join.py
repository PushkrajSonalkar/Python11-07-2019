# Program for split the String and joining the String


def split_string(s):
    a = s.split(' ')
    return a


def join_string(sp):
    string = '_'.join(sp)
    return string


str1 = 'Pushkraj Ravindra Sonalkar'

lis = split_string(str1)
print lis

new = join_string(lis)
print new
