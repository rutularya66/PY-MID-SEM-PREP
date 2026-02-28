t = ()

print(type(t)) # <class 'tuple'>

t = (1)
print(type(t)) # <class 'int'>

t = (1,)
print(type(t)) # <class 'tuple'>


''' 
❌ 2. Thinking tuple cannot contain mutable object

Tuple itself is immutable.

But it can contain list inside it:

t = (1, [2,3])

You cannot change tuple structure.

But you can change list inside it.

Very tricky concept.
'''

t = (1, [2,3])
# t[0] = 100 # TypeError: 'tuple' object does not support item assignment
t[1][0] = 100 # This is changing the list inside the tuple.
print(t) # (1, [100, 3])
# inner list is mutable.


# Tuple has only few methods: count and index. because it cannot be modified.

t = (1,2,3)
t = (4,5) # This is not changing the tuple. its reaassignmnet not midfication.
print(t) # (4, 5)

''''
⚠ Final Important Misconception

Students think:

"Tuple is completely unchangeable."

Correction:

Tuple structure cannot change.
But if it contains mutable object inside, that object can change.
'''