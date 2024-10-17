set1 = {1,2,3,4,5}

# set1[2] = 'Hi' # items can't be accessed by index as set is an unordered data structure

set1.add(12) # adds value
set1.remove(2) # remove value
set1.discard(1) # also removes value

set2 = {4,5,6,7,8}
print(set1.union(set2)) # union operation
print(set1 | set2)

print(set1.intersection(set2)) # intersection operation
print(set1 & set2)

print(set1.difference(set2)) # only those elements in set1 and not in set2
print(set1 - set2)

print(set1.symmetric_difference(set2)) # only elements in either of set1 or set2, but not both
print(set1 ^ set2)