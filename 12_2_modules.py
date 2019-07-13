import sys, fibo

location = dir(fibo)
print(location)
location2 = dir(sys)
print(location2)
import builtins

location3 = dir(builtins)

print(location3)