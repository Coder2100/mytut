#initial sub sequence og the fibonacci series
a,b = 0,1
while a < 10:
    print(a)
    a,b = b, a+b
i = 256 * 256
print('The value of is is', i)

while a < 1000:
    print(a, end=',')
    a,b = b, a+b