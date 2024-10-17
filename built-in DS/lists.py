list1 = [1,2,3,4,5]
# print(*list1)
# print(list1)

# print(*list1,sep=",")

list1.insert(2,44) # index, value

list1.append(45) # at the end of a list

list1.extend([48,49,50]) # accepts a list and extends the existing one

list1.pop(2) # accepts an index to be removed, which is last one by default

del list1[0] # deletes the element at the mentioned index
print(list1)

for x in list1:
    print("Value:",x)