list = [1,2,3,4,5]

# for item in list:
#     print(item,end=" ")

# for idx, item in enumerate(list):
#     print(idx,"index has",item)

# count = 0
# while count < len(list):
#     print(list[count],end=" ")
#     count+=1

count = 0
while count < len(list):
    print(count,"index has",list[count])
    count+=1

# *****
# *****
# *****
# *****
# *****

for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

#     *
#    **
#   ***
#  ****
# *****

for i in range(5):
    for space in range(5-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()