fruits = ["orange", "apple", "pear", "banana", "kiwi", "banana", "banana"]
banana_total = fruits.count('banana')
print(fruits)
absent = fruits.count("love")
print(banana_total)
print(absent)
banana_index = fruits.index("banana")
print(banana_index)
fruits.reverse()

print(fruits)

fruits.append("grapes")
print(fruits)
fruits.sort()

print(fruits)

fruits.pop()

print(fruits)
fruits.insert(1,"granadilla")
print(fruits)