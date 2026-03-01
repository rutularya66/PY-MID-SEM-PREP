# positional arguments

def info(name, age):
    print(name, age)

info("Rutul", 19) # Rutul 19
info(19, "Rutul") # 19 Rutul (order of arguments is important) name = 19, age = rutul wrong meaning.

# default arguments

def info(name, age=18):
    print(name, age)

info("Rutul") # Rutul 18 (age is default)
info("Rutul", 19) # Rutul 19 (age is default but we can override it by passing a value)

# keyword arguments: specify parameter name while calling.

def info(name, age):
    print(name, age)

info(name="Rutul", age=19) # Rutul 19 (order of arguments is not important)
info(age=19, name="Rutul") # Rutul 19 (order of arguments is not important)


def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(1, 2))
print(add(1, 2, 3, 4))

'''
* means:

👉 Collect all extra positional arguments
👉 Pack them into a tuple

Think of it as:
“Take everything and put into one box.”
'''

# args name is just a convention. We can use any name.
# *name, *numbers, *whatever, etc.