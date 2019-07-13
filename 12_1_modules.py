from fibo import fib, fib2
import fibo
from fibo import *
import fibo as fib
from fibo import fib as fibonacci
#fibo.fib(20)
fib(20)
fib(500)
fibonacci(500)


fibo.fib2(100)
print(fibo.__name__)

#If you intend to use a function often you can assign it to a local name:
fib = fibo.fib
fib(500)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
