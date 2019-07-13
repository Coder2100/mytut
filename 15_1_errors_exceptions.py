print("8. Errors and Exceptions")

while True:
    try:
        x = int(input("Enter Integer: "))
        break
    except ValueError:
        print("No a valid integer. Try one more time...")


print(f"You have entered {x}")
    

import sys
try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("could not convert data to an integer.")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise


import sys
try:
    f = open('file2.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("could not convert data to an integer.")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open arg', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x,y = inst.args
    print('x = ', x)
    print('y = ', y)

def this_fails():
    x = 1/0
"""
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error: ', err)

try:
    raise NameError("HiThree")
except NameError:
    print("An exception flew by!")
    raise
print("8.5. User-defined Exceptions")


class Error(Exception):
  #Base class for exceptions in this module.
    pass

class InputError(Error):
   Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
   

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, world!")
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print(f"result is {result}")
    finally:
        print("excuting finally clause")
print(divide(2,2))

print("The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing.")
for line in open("file.txt"):
    print(line)
print("Preferred approach")
with open("file2.txt") as f:
    for line in f:
        print(line)