print("7.1. Fancier Output Formatting")

year = 2016
event = 'referendum'

print(f"Result of the {year} {event} was BREXIT.")

print("The str.format()")

yes_votes =42_572_654
no_votes =43_132_495
percentage_yes = yes_votes/(no_votes + yes_votes)

results = '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage_yes)

print(results)
print("The str() function is meant to return representations of values which are fairly human-readable,")
print("while repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax).")
s = 'Hello World.'

print(str(s))#str

print(repr(s))# intepretor representation
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
hello = 'hello, world\n'
print(s)
hellos = repr(hello)

print(hellos)

print(repr((x, y, ('spam', 'eggs'))))

import math
print(f"The value of pi is approximately {math.pi:.3f}.")

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f"{name:10} ===> {phone:10d}")


animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f"My hovercraft is full of {animals!r}.")

print('We are the {} who say "{}!"'.format('knight', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
#spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
#eggs and spam

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:3d} {1:4d} {2:5d}'.format(x, x*x, x*x*x))

print("Manual String Format")

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
#The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left.
#  There are similar methods str.ljust() and str.center().

print("There is another method, str.zfill(), which pads a numeric string on the left with zeros")
# It understands about plus and minus signs:
print('12'.zfill(5))
print("Old string formatting %s,s as placeholder to the right")
import math
print('The value of pi is approxitaley %5.3f.' %math.pi)




