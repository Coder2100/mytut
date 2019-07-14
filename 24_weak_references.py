import weakref, gc

class A():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

a = A(10)

d = weakref.WeakValueDictionary()
d['primary'] = a 
d['primary']
del a
print(gc.collect())
#d['primary']
print("Tools for Working with Lists")
from array import array

a = array('H', [4000, 10, 700, 22222])
total= sum(a)
print(total)

b= a[1:3]
print(b)
"""The collections module provides a deque() object that is 
like a list with faster appends and pops from the left side
 but slower lookups in the middle.
"""

from collections import deque
d = deque(["tasks", "task2", "task3"])
d.append("task4")
print(d)

print("Handling", d.popleft())
print("Handling", d.popleft())

print("bisect")
"""
unsearched = deque([starting_node])
 def bread_first_search(unsearched):
     node = unsearched.popleft()
     for m in gen_move(node):
         if is_goal(m):
             return m
        unsearched.append(m)

        """
    
import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]

bisect.insort(scores, (300, 'ruby'))

print(scores)

"""The heapq module provides functions for 
implementing heaps based on regular lists. 
The lowest valued entry is always kept at position zero.
"""

from heapq import heapify, heappop, heappush
data = [1,3,5,7,9,2,4,6,8,0]
heapify(data)# rearrange the list into heap order
heappush(data, -5)# add a new entry

[heappop(data) for i in range(3)]
hips = [heappop(data) for i in range(3)]

print(hips)
