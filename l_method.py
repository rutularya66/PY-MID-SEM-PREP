l = [10, 20, 30, 40, 50]

# methods: A function that is associated with an object is called a method.

l.append(60) # append is a method of the list class that adds an element to the end of the list.

print(l) # [10, 20, 30, 40, 50, 60]

# object.method() # object is the name of the object and method is the name of the method.    

a = [1,2]
b = a.append(3) 
print(a) # [1, 2, 3]
print(b) # None 

'''🧠 Mental Rule

If a method modifies list:
It usually returns None.

So NEVER do:

a = a.append(...) '''

b = [1, 2, 3]
a.extend(b) # extend is a method of the list class that adds all the elements of the iterable (list, tuple, etc.) to the end of the list.
print(l.extend(b)) # None
print(l) # [10, 20, 30, 40, 50, 60, 1, 2, 3]



# toonkma a.append print ma lakhso to none aavse.


# insert:
'''list.insert(index, element) # insert is a method of the list class that inserts an element at a specified index in the list. '''

a = [10, 20, 30]
a.insert(1, 99)
print(a) # [10, 99, 20, 30]

# remove:
'''list.remove(element) # remove is a method of the list class that removes the first occurrence of the specified element from the list. '''

a = [10, 20, 30, 20]
a.remove(20)
print(a) # [10, 30, 20]

# pop:
'''list.pop(index) # pop is a method of the list class that removes and returns the element at the specified index in the list. If index is not specified, it removes and returns the last element of the list. '''

a.pop() # removes and returns the last element of the list
print(a) # [10, 30]
a.pop(0) # removes and returns the element at index 0
print(a.pop(0)) # 10
print(a) # [30]

a = [1,2,3,2]
a.remove(2)
x = a.pop(1)
print(a) # [1, 2]
print(x) # 3

''' sort: list.sort() # sort is a method of the list class that sorts the elements of the list in ascending order. '''

b.sort(reverse=True) # sort the list in descending order
print(b) # [3, 2, 1]



''' reverse: list.reverse() # reverse is a method of the list class that reverses the order of the elements in the list. '''

# pop() is the only method that returns "a removed value". All other methods return None.

c = [4, 6, 8, 2]

d = [99, 88, 77]

e = sorted(c)
print(e) # [2, 4, 6, 8]
print(c) # [4, 6, 8, 2]


'''
🔥 One Quick Memory Trick
If method name sounds like ACTION:
append
insert
remove
sort
reverse
Usually returns None.

If it sounds like asking for DATA:
count
index
len
pop (returns removed data)
sorted
Returns something.
'''


k = [1, 2, 3, 4, 5]
print(len(k)) # 5
print(k.count(2)) # 1, Returns how many times a value appears.
print(k.index(3)) # 2, Returns position of FIRST occurrence of value.

# a = [10, "20", 5]
print(max(a)) # TypeError: '>' not supported between instances of 'str' and 'int'

a = [5, 12, 3, 12]

print(max(a))
print(a.index(max(a))) # sorting needs to be done to find the index of the maximum value. If there are multiple maximum values, it returns the index of the first occurrence. In this case, max(a) is 12 and its first occurrence is at index 1. So, a.index(max(a)) returns 1.