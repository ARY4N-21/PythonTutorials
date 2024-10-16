###### Numeric ######

# Integer
x = 10
print(type(x))


# Float
x = 10.43
print(type(x))


# Complex
x = 10 + 10j
print(type(x))


###### Sequence -> Iterables ######


# String
name = "Aryan"
print(name[0])  # Access individual characters
print(type(name))


# List (Array)
example_list = [1,'hello',12.56,1+2j,"ABC"]
print(example_list[0])  # Access index
example_list[1] = "Hi"  # mutable
print(example_list[1])
print(type(example_list))


# Tuples (Immutable list)
example_tuple = (1,'hello',12.56,1+2j,"ABC")
print(example_tuple[0])  # Access index
# example_tuple[1] = "Hi"  # immutable -> will give error
print(example_tuple[1])
print(type(example_tuple))


# Dictionary (Key-value)
dic = {'a' : 22, 'b' : 11.3, 'ab' : 22+11.3}
print(type(dic))
print(dic['ab']) # print value of respective key
print(type(dic['ab'])) #access individual key-value from dict
dic['c'] = 33  # add new key-value to dict
dic['a'] = 'abcd'  # update existing key-value in dict
print(dic)


# Boolean
print(type(True))
print(type(False))


# Set -> Unique non-indexed values, which are immutable and unordered
example_set = {"apple", "banana", "cherry"}
print(type(example_set))
example_set.add('Abcd')
print(example_set)