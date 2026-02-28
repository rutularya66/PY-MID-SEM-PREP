# NUMBER LOGIC PROBLEMS USING LOOPS

# PALINDROME NUMBER

num = 121

temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print('palindrome')
else:
    print('not palindrome')

""" * DIGIT EXTRACTION PATTERN *
while n > 0:
    digit = n % 10
    process digit
    n = n // 10
"""

# ARMSTRONG NUMBER (SUM OF CUBES OF DIGITS = ORIGINAL NUMBER)

num = 153

temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit**3 
    num = num // 10

if temp == sum:
    print('ARMS NUM.')
else:
    print('NOT ARMS NUM.')


# FACTORIAL OF A NUMBER.

num = 5

fact = 1
for i in range (1, num + 1):
    fact = fact * i

print("fact. of", num, "is", fact)


# FIBONACCI SERIES

num = 8

a = 0
b = 1

for i in range(num):
    print(a, end = " ")
    c = a + b
    a = b
    b = c

print()
# PRIME NUMBER

num = 7

if num <= 1:
    print('not prime')
else:
    for i in range(2, num): 
        if num % i == 0:
            print('Not prime')
            break
    else: 
        print('prime')
