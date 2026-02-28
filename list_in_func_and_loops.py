# MIXTURE OF LISTS IN (LOOPS AND FUNCTIONS)


# 1. FIND MAX ELE FROM LIST USING LOOP.

lst = [1, 3, 4, 6, 2]

max_val = lst[0]

for i in lst:
    if i >  max_val:
        max_val = i

print("max ele is:", max_val)


# 1. FIND MAX ELE FROM LIST USING USER-DEFINED FUNCTIONS.

def find_max(list1):
    max_val = lst[0]

    for i in list1:
        if i > max_val:
            max_val = i

    return max_val

# numbers = [6, 293, 385, 219, 158]
# result = find_max(numbers)

result = find_max([6, 293, 385, 219, 158])
print("Max ele is: ", result)
    
    
# 2. SUM OF ELEMENTS IN LIST USING LOOP.

sum = 0

for i in lst:
    sum += i

print('Sum is:', sum)

# same thing using functions

def find_sum(list1):
    total = 0
    
    for i in list1:
        total += i

    return total

result = find_sum([6, 293, 385, 219, 158])
print("Sum is:", result)


# 3. SUM OF EVEN NUMBERS FROM LIST.

even_sum = 0

for i in lst:
    if i % 2 == 0:
        even_sum += i

print('Even Sum is:', even_sum)


# SUM OF ODD NUMBERS FROM LIST.

def find_odd_sum(list1):
    total = 0

    for i in list1:
        if i % 2 != 0:
            total = total + i
    return total

result = find_odd_sum([6, 293, 385, 219, 158])
print("odd sum is:", result)



# 4. COUNT FREQ. OF ELE. IN LIST

l = [1, 3, 6, 8, 3, 2]
''' NOT CLEAN, reason: 3 appeared 2 times will be printed twice.
for i in l:
    count = 0
    for j in l:
        if i == j:
            count += 1
    print(i, 'appeared', count, 'times')
'''
checked = []

for i in l: # OUTER LOOP FOR PICKING ELE. 
    if i not in checked:
        count = 0
        for j in l: # FOR COUNTING ELE.
            if i == j:
                count += 1
        print(i, 'appeared', count, 'times')
        checked.append(i)

# USING FUNC.

def count_freq(list1):
    freq = {} # here dictionary used to cleanly show count of each value in (key : value) pair.

    for i in list1:
        if i not in freq:
            count = 0
            for j in list1:
                if i == j:
                    count += 1
            freq[i] = count
    return freq

result = count_freq([6, 293, 385, 6, 385, 219, 158])
print(result)



        

# 5. REMOVE DUPLICATE VALUES FROM LIST.

unique = []

for i in l:
    if i not in unique:
        unique.append(i)

print("Updated list after op.", unique)

# Using FUNC.

def remove_duplicates(list1):
    unique = []

    for i in list1:
        if i not in unique:
            unique.append(i)

    return unique

result = remove_duplicates([6, 293, 385, 6, 385, 219, 158])
print("After removing duplicates the updated list is:", result)

# 6. SEARCH ELEMENT IN LIST.

goal = 4
found = False

for i in l:
    if i == goal:
        found = True
        break

if found:
    print("Yeah We got it")
else:
    print("We couldn't find it")


# BY USING FUNC.

def search_element(list1, key):
    for i in list1:
        if i == key:
            return True
    return False

result = search_element([6, 293, 385, 219, 158], 219)

if result:
    print("Ele. Found")
else:
    print("Ele. not found")


    
# 7. REVERSING THE LIST.

# M - 1
rev = []

for i in l:
    rev.insert(0, i) # inserting new ele at index 0.
    
print("Reversed list:", rev)

# M -2
l2 = [1, 6, 2, 3, 8]
rev = []

for i in range(len(l2)-1, -1, -1):
    rev.append(l2[i])

print("Reversed list:", rev)


# UsING FUNC.

def reverse_list(list1):
    rev = []

    for i in range(len(list1)-1, -1, -1):
        rev.append(list1[i])

    return rev

result = reverse_list([1, 5, 19, 2, 4])
print("The reversed list is:", result)
    



'''8. Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings. '''

l = ['racecar', 'abc', 'aa', '151', 'v', 'k']
count = 0

for i in l:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("Count is:", count)
        

# USING FUNC.


def count_strings(list1):
    count = 0

    for i in list1:
        if len(i) >=2 and i[0] == i[-1]:
            count += 1

    return count

result = count_strings(['racecar', 'abc', 'aa', '151', 'v', 'k'])
print('Count is:', result)
