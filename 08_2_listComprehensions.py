#5.1.1. Using Lists as Stacks¶

#To add an item to the top of the stack, use append()
#To retrieve an item from the top of the stack,
#use pop() without an explicit index
stack = [3, 4, 5]
print(stack)
stack.append(6)
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#5.1.2. Using Lists as Queues
#It is also possible to use a list as a queue
# first element added is the first element retrieved 
# (“first-in, first-out”);

from collections import deque
queue = deque(["Zukile", "Nqwenelwa", "Odwa","Sam","Aphelele"])
queue.append("Qhawe")
print(queue)
queue.append("Zakum")
print(queue)
queue.popleft()
print(queue)#in order of arrival

#5.1.3. List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
#calculate list pf squrs
squares_lambda = list(map(lambda x:x**2, range(10)))
print(squares_lambda)
#readable as:
squares_range = [x**2 for x in range(10)]
print(squares_range)
vec = [-4, -2, 0, 2, 4]
#create a new list with the values doubled
vec = vec *8
print(vec)

#nested list comprehension

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print(matrix)