words = ['cat','window','milk']

for word in words:
    print(word, len(word))
#modify forloop

#create a copy first
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 4:
        words.insert(0, w)
print(words)
print()
for i in range(0,5):
    print(i)
#To iterate over the indices of a sequence, you can combine range() and len()
print()
a = ['Zukile', 'Nqwesh', 'Monwabisi', 'Odwa']
for i in range(len(a)):
    print(i+1, a[i])

#to get range
print(range(10))
#for loop is an iterator
#list() if an iterator too
print(f" list() iterator {list(range(10))}")

#break
for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x , '*', n//x)
            break
    else:
        #loop fell through without finding a factor
        print(n, 'is prime number')

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("found a number ", num)