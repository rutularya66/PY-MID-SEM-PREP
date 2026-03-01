def add(a, b):
    total = a + b
    return total

result = add(14, 5)
print("Result is:", result) # 19


def add(a, b):
    total = a + b
    return total

result = add(14, 5)
# print("Result is:", total) # NameError: name 'total' is not defined


def add(a, b):
    total = a + b
    print(" total is:", total) 

result = add(14, 5)
print("Result is:", result) # None


def add(a, b):
    total = a + b
    return total
    print("hi") # UNREACHABLE CODE

result = add(14, 5)
print("Result is:", result)


def add(a, b, c):
    total = a + b
    return total
    increment += a

# result = add(14, 5)
# result2 = add(5) # TypeError: add() missing 1 required positional argument: 'b'

# result = add(14,5)
print("Result is:", result) #TypeError: add() missing 1 required positional argument: 'c'


def test():
    x = 5
    print(x)

test() # 5
# print(x) # NameError: name 'x' is not defined

'''
Important Understanding

Function name → Used to CALL the function
Variable names → Used inside to do calculation

They are different things.
'''

'''
Important Understanding

Function name → Used to CALL the function
Variable names → Used inside to do calculation

They are different things.
'''


'''
Now Very Important Case
If you try to modify global without saying global:
'''
x = 100

def test():
    x = x + 1
    print(x)

test() # UnboundLocalError: local variable 'x' referenced before assignment
''''
This gives error.
Because:

Python sees x = x + 1
It thinks:
"Oh, x is local because you are assigning it."
But before assigning,
you are trying to use it.

So error.
'''

# So What Is Purpose of Local Variable?

'''
Purpose:
✔ Keep function independent
✔ Avoid changing outside variables accidentally
✔ Avoid confusion
✔ Safer programming

Imagine 1000 lines program.
If every function changes global variables,
everything becomes messy.

Local variables protect structure.
'''

'''
So How Do We Actually Modify Global?
We tell Python explicitly:

x = 100

def test():
    global x
    x = x + 1
    print(x)

test()
print(x)

Now Python understands:
"Use global x."
Output:
101
101
'''


x = 10

def test():
    print(x)
    x = 5

test() # UnboundLocalError: local variable 'x' referenced before assignment

'''
Python does NOT decide scope line by line at runtime.

It decides scope BEFORE running the function.

When Python sees inside function:
x = 5

It immediately marks x as LOCAL for the whole function.

So internally Python thinks:
 
def test():
    local x
    print(x)
    x = 5
 
    now when print(x) runs,
it tries to print local x.

But local x has no value yet.
So error:
UnboundLocalError
 '''
'''
Think Like This (Very Easy Analogy)

Function says:

"I will use my own x."

But before giving its own x any value,
it tries to print it.

So Python says:
"I don’t know this x yet."

Error.'''

def add(a, b):
    return a + b

if add(2, 3) > 4:
    print("Greater") # Greater

if add(2, 3) > 5:
    print("Greater") # Not printed because condition is False


def add(a, b):
    return a + b

print(add(4, 6)) # 10
x = add(4, 6) 
print(x) # 10


def add(a, b):
    print(a + b)

x = add(4, 6)   
print(x) # None

print(add(4, 6)) # 10

def add(a, b):
    c = a + b
'''
This calculates c.
But after function ends,
c disappears.

Nothing comes outside.

So outside world doesn’t know the result.

Return is how we bring result outside.
'''

def add(a, b):
    c = a + b
    print(c) # 10
    return c # 

if add(1,2) > 4:
    print("Yes") # Not printed because 3 is not greater than 4


