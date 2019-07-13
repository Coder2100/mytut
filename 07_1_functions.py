#definig fibonacci series

def fib(n):
    a,b = 1,2
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)
# function that return list of numbers
def fib2(n):
    #create empty list
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f100 = fib2(100)
print(f100)