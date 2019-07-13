print("Scopes and Namespaces Example")

def scope_test():
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()

    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)

class MyClass:
    #a simple class example
    i = 12345
    def f(self):
        return 'hello world'
        #instanstiate the class
        x = MyClass()
      #  print(x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
call = x.r, x.i
print(call)
print()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)

del x.counter
#print(x.counter)

class Dog:
    kind = 'canine'# class variable shared by all instances

    def __init__(self, name):
        self.name = name  #instance variable unique to each instance
d = Dog('Deggy')
e = Dog('Bhubesi')
w = Dog('Whisky')
d.kind
print(d.kind)
e.kind
print(e.kind)

d.name
print(d.name)
e.name
print(e.name)
print(w.name)

class Cattle:
    tricks = []
    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Cattle('Dibesi')
g = Cattle('Gwedlani')
w = Cattle('Wasakaza')
d.add_trick('Iyagquba')
g.add_trick('Iyakhala')
w.add_trick('Yancancisa')
d.tricks # unexpectedly shared by all dogs
print(d.tricks)
print("Correct design of the class should use an instance variable instead:")

class Dog2:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

d.tricks
print(d.tricks)

e.tricks
print(e.tricks)

class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def addwice(self, x):
        self.add(x)
        self.add(x)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update # private copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
        #return super().update(iterable)


class Employee:
    pass
john = Employee() #create an empty employee
# fill the fields of the records
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 2000

print("Iterators:")
for element in [1,2,3,4]:
    print(element)
for element in (1,2,3,4):
    print(element)

for key in {'one':1, 'two':2, 'three':3, 'four':4}:
    print(key)

numbers = {'one':1, 'two':2, 'three':3, 'four':4}
for k,v in numbers.items():
    print(f"{k} <====> {v}")

for char in "ZUKILE MTOTSO":
    print(char)

for line in open('file2.txt'):
    print(line, end=' ')
s = 'abc'
it = iter(s)
print(it)
next(it)
next(it)
print(next(it))

class Reverse:
    #Iterator for looping over a sequence backwards.

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)

print(iter(rev))

for char in rev:
    print(char)

print("9.9. Generators")

#Generators are a simple and powerful tool for creating iterators. 

#They are written like regular functions but
#  use the yield statement whenever they want to return data. 

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

mysum = sum(i * i for i in range(10)) # # sum of squares
print(mysum)

xector = [10,20,30]
yector = [7,5,3]
double_looping = sum(x*y for x,y in zip(xector,yector ))

print(double_looping) # dot product

from math import sin, pi
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table )
#unique_word = set(word  for line in page  for word in line.split())
#print(unique_word)
#valedictorian = max((student.gpa, student.name) for student in graduates)
#print(valedictorian)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))