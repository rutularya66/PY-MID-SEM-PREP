l = [1, 5, 2, 4]

l[0] = 2

print(l)

##l[8] = 4

name = "RP"

# name[0] = "R"

print(name)

print(l)

a = [1, 2, 3]
b = a
b[0] = 100 # a[0] = 100 
print(a) 
print(b)
b.append(200)
print(a) # a = [100, 2, 3, 200]
print(b) # b = [100, 2, 3, 200]

a = [5, 6, 7]
b = a
a = [1, 2, 3]
b[0] = 100
print(a) # a = [1, 2, 3]
print(b) # b = [100, 6, 7]

a = 10
b = 20
b = a # b = 10
print(a) # a = 10
print(b) # b = 10

a = [5, 6]
b = a
a = [1, 2]
b[0] = 100
print(a) # a = [1, 2]
print(b) # b = [100, 6]

l =[ 10, 20, 30,  40, 50]
print(l[:]) # [10, 20, 30, 40, 50]
# l[:] creates a new list that is a copy of the original list l.
# start = 0 for default and end = len(l) for default.
print(l[:5]) # [10, 20, 30, 40, 50]

# methods: A function that is associated with an object is called a method.

l.append(60) # append is a method of the list class that adds an element to the end of the list.

print(l) # [10, 20, 30, 40, 50, 60]

object.method() # object is the name of the object and method is the name of the method.    


