# MIXTURE OF LISTS AND LOOPS.


# FIND MAX ELE FROM LIST USING LOOP.

lst = [1, 3, 4, 6, 2]

max_val = lst[0]

for i in lst:
    if i >  max_val:
        max_val = i

print("max ele is:", max_val)

    
# SUM OF ELEMENTS IN LIST USING LOOP.

sum = 0

for i in lst:
    sum += i

print('Sum is:', sum)

# SUM OF EVEN NUMBERS FROM LIST.

even_sum = 0

for i in lst:
    if i % 2 == 0:
        even_sum += i

print('Even Sum is:', even_sum)

# COUNT FREQ. OF ELE. IN LIST

l = [1, 3, 6, 8, 3, 2]
'''
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

# REMOVE DUPLICATE VALUES FROM LIST.

unique = []

for i in l:
    if i not in unique:
        unique.append(i)

print("Updated list after op.", unique)


# SEARCH ELEMENT IN LIST.

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


# REVERSING THE LIST.

# M - 1
rev = []

for i in l:
    rev.insert(0, i) # inserting new ele at index 0.
    
print("Reversed list:", rev)

# M -2
rev = []

for i in range(len(l)-1, -1, -1):
    rev.append(l[i])

print("Reversed list:", rev)


'''Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings. '''

l = ['racecar', 'abc', 'aa', '151', 'v', 'k']
count = 0

for i in l:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("Count is:", count)
        


