def sumFn(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sumFn(1,2,4,3,4))
print(sumFn(1,2,3))

########### KWARGS ##############

def sumFn2(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum,1)

print(sumFn2(A = 12, B = 24, C = 36.58))