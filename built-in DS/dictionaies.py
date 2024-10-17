dict1 = {1:"Coffee", 2:"Tea", 3:"Juice","Name":"Aryan",1:"Chai"} # overrides the older key with the new assigned value
print(dict1[1]) # Coffee

dict1[2] = "Mint Tea"
print(dict1)

del dict1[3]
print(dict1)

# Iterating a dictionary

for key,value in dict1.items():
    print(key,':',value)