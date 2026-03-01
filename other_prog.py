'''
filter() is a built-in function in Python.

It is used to:

Select elements from a sequence

Based on a condition (True / False)

It does not modify data.
It returns only those elements for which the condition is True.

'''
'''
syntax:
filter(function, iterable)
'''

'''
Working of filter()

For every element in the iterable:

1. The function is applied.
2. If the function returns True → element is kept.
3. If False → element is removed.

The result must be converted into a list using list() if we want to print it properly.
'''

# Program: Find Prime Numbers in a Given Range Using filter.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = 10
end = 30

numbers = range(start, end + 1)

prime_numbers = list(filter(is_prime, numbers))

print("for in given range avibhajay sankhyao :", prime_numbers) # [11, 13, 17, 19, 23, 29]


# Program: Find Armstrong Numbers in a Given Range Using map()


def check_armstrong(n):
    temp = n
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp = temp // 10
    
    if total == n:
        return n
    else:
        return None


start = 100
end = 500

numbers = range(start, end + 1)

armstrong_list = list(map(check_armstrong, numbers))

# Remove None values
armstrong_list = [x for x in armstrong_list if x is not None]

print("Armstrong numbers:", armstrong_list) # [153, 370, 371, 407]  

'''
🟦 Explanation of Program

check_armstrong(n):

Extracts each digit using % 10

Cubes the digit

Adds to total

Compares total with original number

map(check_armstrong, numbers):

Applies function to each number in range.

Returns either the number (if Armstrong) or None.

Since map() does not remove elements,
we remove None values using list comprehension.
'''