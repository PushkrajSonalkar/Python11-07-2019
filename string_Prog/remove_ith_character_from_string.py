# remove ith character from string

str1 = raw_input("Enter a string\n")
print "Original string is :", str1
new_s = ""
length = len(str1)
pos = int(raw_input("Enter position of character to remove\n"))
for i in range(0, length):
    if i != pos-1:
        new_s = new_s + str1[i]

print new_s
