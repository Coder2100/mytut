
#lambda functions can be created with the 'lambda' keyword
#Lambda functions can be used wherever function objects are required
#They are syntactically restricted to a single expression
# Like nested function definitions, 
# lambda functions can reference variables from the containing scope

# lambda expression to return a function
def make_increment(n):
    return lambda x: x +n
f = make_increment(42)
f(0)
f(1)
print(f(0))
print(f(1))

#Another use is to pass a small function as an argument

pairs = [(1, 'one'), (2,'two'), (3,'three'), (4,'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
print(pairs)