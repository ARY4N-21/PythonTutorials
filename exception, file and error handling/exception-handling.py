# In python, exception is a type of error, which happens while code running, and are not alerted by the IDEs.
# Example, dividing a number by 0 will give division by ZeroDivision Exception

def division(a,b):
    return a/b

try:
    print(division(12,0))
except ZeroDivisionError as e: # specific exception
    print("Error: ", e)
except Exception as e: # e is an alias to exception
    print(f"Error: {e}")
    print(e.__class__) # class of exception



items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except IndexError:
    print("Item does not exist in the list")



def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(0)
    except Exception as e:
        print("Error",e)


ans = divide_by(40, 0)
print(ans)



try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  