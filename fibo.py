#fibonacci numbers module

def fib(n):# fibonacci write series aup to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()#skip a line

def fib2(n):
    result = []
    a, b = 0, 1
    while a< n:
        result.append(a)
        a,b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

#run python fibo.py 50