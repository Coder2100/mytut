def ask_ok(prompt, retries=4, reminder='Please try agin!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries -1

        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
#ask_ok()

i = 5

def f(args =i):
    print(args)

i = 6
f()

#default argument evaluate once
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
#If you don’t want the default to be shared between subsequent calls,

def f2(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L

print(f2(1))
print(f2(2))
print(f2(3))

#Keyword Argument
def parrot(voltage, state='a stiff', action='voom', type='Nowey Brue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, 'volt through it.')
    print('-- Lovely plumage, the', type)
    print("-- It's", state, "!")
parrot(100)