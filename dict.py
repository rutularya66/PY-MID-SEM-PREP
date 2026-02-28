'''
What is a Dictionary?

A dictionary stores data in key–value pairs.

Instead of index numbers like list,
it uses keys to access values.
'''

d = {
    "name": "Rutul",
    "age": 19
}


'''
"name" → key

"Rutul" → value

"age" → key

19 → value
'''

'''
Important Characteristics:
✔ Uses { }
✔ Stores data as key : value
✔ Keys must be unique
✔ Mutable
✔ Ordered (in modern Python)
'''

print(d) # {'name': 'Rutul', 'age': 19}
print(type(d)) # <class 'dict'>

o = {}
print(type(o)) # <class 'dict'>

print(d["name"]) # Rutul
print(d["age"]) # 19
# print(d["Rutul"]) # KeyError: 'Rutul' because there is no key named "Rutul" in the dictionary.


d["Surname"] = "Arya" # Adding a new key-value pair to the dictionary.
print(d) # {'name': 'Rutul', 'age': 19, 'Surname': 'Arya'}


d["age"] = 21 # Modifying the value of an existing key in the dictionary.
print(d) # {'name': 'Rutul', 'age': 21, 'Surname': 'Arya'}


'''
Important Rule

Dictionary uses:
dictionary[key] = value
This is used for both:
Adding
Updating

Students often think separate method exists — but no.
'''

# Removing data:
# pop() -- removes by key and returns the value.

# x = d.pop() # KeyError: pop expected at least 1 argument, got 0 because pop() requires a key argument to specify which key-value pair to remove from the dictionary.

x = d.pop("age") # removes the key "age" and returns its value (21)
print(x) # 21
print(d) # {'name': 'Rutul', 'Surname': 'Arya'} 

# del(): Does NOT return value.
del d["name"] # removes the key "name" and its associated value from the dictionary.
print(d) # {'Surname': 'Arya'}



'''
Important Dictionary Methods
1️⃣ keys()
d = {"a":1, "b":2}
print(d.keys())

Output:

dict_keys(['a', 'b'])

Returns all keys.

2️⃣ values()
print(d.values())

Returns all values.

3️⃣ items()
print(d.items())

Returns pairs like:

('a',1), ('b',2)
'''

s = {"kumar": [1,2,3]}
print(s) # {'kumar': [1, 2, 3]}

# f = {[1,2,3]: "kumar"} # TypeError: unhashable type: 'list' because lists are mutable and cannot be used as keys in a dictionary.

f = {(1,2,3): "kumar"} # This is valid because tuples are immutable and can be used as keys in a dictionary.
print(f) # {(1, 2, 3): 'kumar'}



d = {"x":10, "y":20}
d["x"] = 50
d["z"] = 100
print(d) # {'x': 50, 'y': 20, 'z': 100}


# NESTED DICTIONARY

student = {
    "name": "Rutul",
    "marks": {
        "math": 90,
        "science": 85
    }
}


print(student["marks"]) # {'math': 90, 'science': 85}
print(student["marks"]["math"]) # 90

student["address"] = {"city": "Ahmedabad", "pin": 380001}
print(student) # {'name': 'Rutul', 'marks': {'math': 90, 'science': 85}, 'address': {'city': 'Ahmedabad', 'pin': 380001}}


employees = {
    "emp1": {"name": "A", "salary": 20000},
    "emp2": {"name": "B", "salary": 25000}
}

print(employees["emp1"]["name"]) # A
print(employees["emp2"]["salary"]) # 25000