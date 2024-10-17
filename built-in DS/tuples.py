tuple1 = (1,'string',4.55,True)

print(tuple1[1]) # pass the index of element you want to access
print(tuple1.count(4.55))  # returns the count of a specific element
print(tuple1.index('string'))  # return the index of a specific value


for x in tuple1:
    print(x,end=", ")

# the main diff b/w tuple and list is tuple is immutable