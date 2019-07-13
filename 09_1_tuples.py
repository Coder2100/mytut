print("5.3. Tuples and Sequences")

#example of tuple packing
t = 1223, 65656, 'Helo'

print(t[0])
print(t)
print("tuples may be nested")
u = t, (1,2,3,4,5,6)
print(u)
print('tuples are immutable')
empty = ()
singleton = 'Hello'
print(f"The length of {len(empty)}")
print(f"The length of singleton = 'Hello' {len(singleton)}")

