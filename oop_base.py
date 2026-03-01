# BASE PROGRAM (class + object + self + init)

class student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = student("Rutul")
s1.display() # Name: Rutul
'''
This single example will help us answer:

What is class?
What is object?
What is self?
What is init?
What is constructor?
What is type(object)?

Same program. Just explanation changes.
'''

# Inheritence Program

class Person:
    def show(self):
        print("I am a perosn")

class Student(Person):
    def display(self):
        print("I am a student")

s = Student()
s.show() # I am a perosn
s.display() # I am a student

'''
This will help in:

Explain inheritance
Types of inheritance
super keyword
Program based question
Output tracing

'''


'''

Real World Example

Suppose I say:

👉 "Student"

Now tell me:

Is this one specific person?
No.

It is just a general idea / blueprint.

It does not represent any specific student.

Now suppose:

Student 1: Rutul, Roll 21
Student 2: Amit, Roll 22

These are real persons.

So:

"Student" → Blueprint

Rutul → Real instance

Amit → Real instance
'''
'''
So What Is Class?

Class is a blueprint / template.

It defines:

What data will exist

What functions will exist

But it does not create real data yet.

🔹 What Is Object?

Object is a real instance created from class.

When we create object:

Memory is allocated

Data becomes real

'''

'''Q. CALSSES IN PYTHON
A class in Python is a user-defined data type that acts as a blueprint for creating objects. It is used to group data (variables) and functions (methods) together into a single unit.

In simple words, a class defines what properties and behaviors an object will have, but it does not create any real data until an object is created.

Syntax of Class:
class ClassName:
    # data members
    # member functions

The keyword class is used to define a class.

Class name should start with capital letter (by convention).

Methods inside class must have self as first parameter.




Important Points:

Class is a blueprint for objects.

Object is an instance of a class.

Data and functions are defined inside class.

Object is created using ClassName().

Methods are accessed using object name.

Advantages of Class:

Improves code organization.

Promotes reusability.

Supports Object Oriented Programming.

Makes program modular and easy to maintain.
'''



'''
1️⃣ Function and Method – Are They Same?

Very simple:

✔ A function is written outside class.
✔ A method is a function written inside a class.

That’s the only difference.


4️⃣ What is Class Actually?

Let’s remove confusion.

When you write:

class Student:
    pass

You are defining a new type.

Just like:

int
float
str

Student becomes a new data type.

Then:

s1 = Student()

means:

Create object of type Student.


'''
'''
 class Student2:
    def greet(name):
        print("Hello", name)

s1 = Student2()
s1.greet("Rutul") # TypeError: greet() takes 1 positional argument but 2 were given
'''

'''
this gives error because python secretly converts it to:

Student.greet(s1, "Rutul")
Very important.

So Python automatically sends the object (s1) as first argument.

Now count arguments:

We passed:

s1 (automatically)
"Rutul"

Total = 2 arguments

But our function definition has only 1 parameter:

def greet(name):
So mismatch happens → error.

'''
'''
Why Name self?

It is just a convention.

We could write:

def greet(obj, name):

It would still work.

But everyone writes self.

So:

self is just the first parameter
that receives the calling object.

Nothing magical.
'''

'''
Parameter vs Argument (No confusion)

When we define a function:

def greet(name):

name → Parameter

When we call the function:

greet("Rutul")

"Rutul" → Argument

So:

Parameter = variable inside definition

Argument = value we pass while calling

I used both words because they mean different things.
But don’t worry too much — just remember this difference.

'''

class Student:
    def greet(self, name):
        print(self)
        print(name)

s1 = Student()
s1.greet("Rutul") # <__main__.Student object at 0x7f8c8c8c8c8>
# Rutul

'''
Output will show:

memory address of s1

Rutul

So inside function:

self is just a normal variable
that holds the object reference.

Nothing else.'''

# func normally vs inside class

# normal func

def greet(name):
    print("Hello", name)

greet("Rutul")

# calling style
#function_name()

# func inside class(method)

class Student:
    def greet(self, name):
        print("Hello", name)

s1 = Student()
s1.greet("Rutul")
# calling style
# object.method()

'''
Why?

Because the method belongs to the object.

It is not free-floating.

Think like this:

Normal function → lives alone
Method → lives inside object

So you must go through the object to use it.

'''
'''
Now Let’s Remove Fear

This:

greet("Rutul")

and this:

s1.greet("Rutul")

are conceptually SAME.

Only difference:

Second one automatically sends object also.
'''

'''
Step 2: What does the object look like?

Right after:

s1 = Student()

Object is like:

Student object
(Empty)

No name.
No roll.
Nothing.

Just empty container.

🟢 Step 3: Now See This Code
class Student:
    def set_name(self, name):
        self.name = name

s1 = Student()
s1.set_name("Rutul")

Now slow down.

When this runs:

s1.set_name("Rutul")

Python sends:

s1 → into self

"Rutul" → into name

So inside function:

self = s1
name = "Rutul"

Now look at this line carefully:

self.name = name

Replace values:

s1.name = "Rutul"

That means:

Inside object s1,
create a variable called name
and store "Rutul" in it.
'''

'''
Important

self.name is just:

Object + dot + variable

Like:

s1.name

Same thing.

Inside class we write self.name
Outside class we write s1.name

🧠 Final Clean Idea

s1 = Student() → create empty object

self.name = name → put data inside object

No relation with return

self = current object

'''


'''
Important Thing

__init__() is NOT creating object.
Object is created first.
Then __init__() runs to initialize it.

Think like:

Step 1 → Build empty house
Step 2 → Furnish it (__init__())

🟢 Common Confusion

❌ Thinking __init__() creates object
❌ Thinking we must call it manually
❌ Thinking it returns something

It returns nothing.
It just sets up the object.
'''

class Student:
    def __init__(self, name):
        self.name = name
      
# s1 = Student() # TypeError: __init__() missing 1 required positional argument: 'name'
