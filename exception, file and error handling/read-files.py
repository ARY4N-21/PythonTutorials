# Python has 3 read methods
# 1) read()
# 2) readline()
# 3) readlines()
with open('file.txt','r') as file:
    # print(file.read())
    # prints a string containing all characters, also accepts int arg, for limit of characters to be printed
    print(file.read(10))


with open('file.txt','r') as file:
    print(file.readline()) # only first line from file, similar arg as read()

with open('file.txt','r') as file:
    print(file.readlines())
    # this returns the file content in a ordered manner, spearating lines with linebreaks, and returns the data in form of list

