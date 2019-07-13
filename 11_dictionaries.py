#dictionry = key:value pair
# list(d) on a dictionary returns a list of all the keys used in the dictionary,

#if you want it sorted, just use sorted(d) instead)

#To check whether a single key is in the dictionary, 
# use the in keyword.
tel = {'jack':4098, 'sape':4534}
print(tel['jack'])
tel['zukile'] = 278409784
print(tel)
del tel['sape']
print(tel)
tel['odwa'] = 9585
print(tel)
#convert into list or return list

print(list(tel))#get keys
print(sorted(tel)) # get is sorted

print("search using the 'in' key word")
print(('zukile' in tel))
print(('sam' in tel))
print(('zukile' not in tel))
print(('sam' not in tel))
print('The dict() constructor builds dictionaries directly from sequences of key-value pairs:')

dictonry = dict([('zukile', 4332), ('sam', 984), ('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dictonry)

print(({x: x**2 for x in (2, 4, 6)}))
#hen the keys are simple strings,
#  it is sometimes easier to specify pairs using keyword arguments:
short = dict(sape=4139, guido=4127, jack=7484)
print(short)
print("When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method")
oldies = {'zuks':28, "sam":18, "wise":24, "ap":15}
for k,v in oldies.items():
    print(k,v)

print("When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print("To loop over two or more sequences at the same time, the entries can be paired with the zip() function.")

questions = ['names', 'quest', 'favorite color']
answers = ['lcaoste', 'success', 'blue']

for q , a in zip(questions, answers):
    print('what is your {0}? It is {1}.'.format(q,a))

print("To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.")
for i in reversed(range(0,10,2)):
    print(i)

print("To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.")
basketz = ['guava', 'pesika', 'granadilla','apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#looping a sorted list

for f in sorted(set(basketz)):
    print(f)
print("It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.")
import math
raw_data = [56.2, float('NaN'), 51.7,56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filter_data = []
for value in raw_data:
    if not math.isnan(value):
        filter_data.append(value)
print(raw_data)
print(filter_data)
