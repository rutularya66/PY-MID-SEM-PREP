# 1. (V.IMP) ARMSTRONG NUMBER:
'''
num = int(input("Enter number: "))   # take input from user

temp = num        # copy original number (we will change temp, not num)
sum = 0           # to store sum of cubes

while temp > 0:   # loop runs until all digits are processed
    
    digit = temp % 10      # get last digit
    sum = sum + digit**3   # add cube of that digit
    
    temp = temp // 10      # remove last digit

# after loop, compare result with original number
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
'''




# 2. (IMP) PALINDROME NUMBER: A palindrome number is a number that reads the same backward as forward. For example, 121 is a palindrome, while 123 is not.
''''
num = int(input("Enter number: "))   # take input

temp = num        # copy original number
reverse = 0       # to build reversed number

while temp > 0:   # loop until all digits are used
    
    digit = temp % 10              # get last digit
    reverse = reverse * 10 + digit # build reverse number
    
    temp = temp // 10              # remove last digit

# compare original and reversed number
if reverse == num:
    print("Palindrome number")
else:
    print("Not a palindrome number")
'''




# 3. (AVG) FIBONACCI SERIES UPTO N TERMS:
'''
n = int(input("Enter number of terms: "))  # how many terms

a = 0 # first number
b = 1 # second number

count = 0

while count < n:
    print(a, end = ' ')  # print current number, end=' ' keeps it on the same line
    next = a + b      # next number is sum of previous two
    a = b             # shift a to forward
    b = next          # shift b to forward
    count += 1        # increment count, as we have printed one term
    
# OUTPUT: Enter number of terms: 8
# 0 1 1 2 3 5 8 13
'''



# 4. (AVG) SUM OF A PARTICULAR RANGE USING reduce() FUNCTION:

# The reduce() function is a part of the functools module in Python and is used to apply a specified function cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value. In this case, we can use reduce() to calculate the sum of a range of numbers.
'''
from functools import reduce   # import reduce function

start = int(input("Enter start: "))   
end = int(input("Enter end: "))      

numbers = range(start, end + 1)       # here, end + 1 is used because range() does not include the end value, so we add 1 to include it.

result = reduce(lambda x, y: x + y, numbers)

print("Sum is:", result)   
# OUTPUT: Enter start: 1
# Enter end: 5
# Sum is: 15
'''


# 5. (AVG)ACCEPT A SENTENCE AND CALCULATE THE NUMBER OF LETTERS AND DIGITS.
'''
sentence = input("Enter a sentence: ")

letters = 0 # to count letters
digits = 0 # to count digits

for char in sentence:  # iterate through each character in the sentence
    if char.isalpha():  # check if it's a letter
        letters += 1
    elif char.isdigit():  # check if it's a digit
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)

# OUTPUT: Enter a sentence: hello123
# Number of letters: 5
# Number of digits: 3

'''

# 10. (AVG) EVEN NUMBERS IN SPECIFIC RANGE USING filter() FUNCTION:

start = int(input("Enter start: "))
end = int(input("Enter end: "))

numbers = range(start, end + 1)  # create a range of numbers from start to end

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # filter even numbers using lambda function

print("Even numbers in the range:", even_numbers)

# OUTPUT: Enter start: 2
# Enter end: 13
# Even numbers in the range: [2, 4, 6, 8, 10, 12]
