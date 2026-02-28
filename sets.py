#What is a Set?

#A set is:

# A collection of unique values stored inside,  { }.

p = {1, 2, 2, 3, 4, 6,  5, 6, 9, 8, 9}
print(p) # {1, 2, 3, 4, 5, 6, 8, 9}, order may change.

# so no indexing.

'''
Most Important Properties of Set

✔ Uses { }
✔ Stores only UNIQUE values
✔ Unordered
✔ Mutable
✔ No indexing
'''

s = {}
print(type(s)) # <class 'dict'>, this is not a set, this is an empty dictionary.
s = set()
print(type(s)) # <class 'set'>, this is an empty set.


p.add(100) # add is a method of the set class that adds an element to the set.
print(p) # {1, 2, 3, 4, 5, 6, 8, 9, 100}, order may change.

p.remove(231) # removes value, error if not found.

p.discard(231) # removes value, does not error if not found.


# IMP SET OPERATIONS.
# output written inside set.

'''
union: a | b
intersection: a & b
difference: a - b
'''

# more...
p.pop() # removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
print(p) # {2, 3, 4, 5, 6, 8, 9, 100}, order may change.


# subset & superset
a = {1,2}
b = {1,2,3}

print(a.issubset(b))   # True
print(b.issuperset(a)) # True

# Converting List to Set (Common Usage)
# Very common trick to remove duplicates.

a = [1,2,2,3]
s = set(a)
print(s)

# Output:

{1,2,3}
