squares = [1,4,9,16,25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])

#lists are mutable while strings are immutable
squares = squares + [36, 49, 64, 81, 100]

print(squares)
cubes = [1,8,27,65,125] # 
numb = 4 **3
cubes[3] = numb

print(cubes)
#use append to add new items of the list(it get added at end of the list)

#cubes[4] = cubes.append(64)# this return None in .py
letters = ['a','b','c','d','e','f','g','h']
print(letters)

letters[2:5] = ['C','D','E']
print(letters)
letters[2:5] = []# remove spcified arrays
print(letters)
letters[:] = []# clear the list by replacing all the elements with an empty list
print(letters)
alphabets = ['a','b','c','d']
print(f"The length of list alphabets = ['a','b','c','d'] is {len(alphabets)}.")

a = ['a','b','c','d']
n = [1,2,3]
x = [a,n]

print(f"The combined list of x is  {x}.")
print(f" The first item List {x[0]}")
print(f"The second Item List {x[1]}")
print(f"getting first index {x[0][1]}")
