print("5.4. Sets")
#Python also includes a data type for sets. 
# A set is an unordered collection with no duplicate elements.
#Basic uses include membership testing 
# and eliminating duplicate entries.
#create set use set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print(('orange' in basket))
a = set('amasi')
b = set('banana')
print(a)## unique letters in a
print(b)# unique letters in b
aa = a -b # letters in a but not in b
print(aa)
ab = a | b# letters in a or b or both
print(ab)
bb = a & b## letters in both a and b
print(bb)
aabb =  a ^ b# letters in a or b but not both
print(aabb)## letters in a or b but not both

print("List comprehension supported")
listcompr = {x for x in "elliotdale" if x not in 'bsc'}
print(listcompr)