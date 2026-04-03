# 6. (IMP) REMOVE DUPLICATE VALUES FROM A LIST USING USER-DEFINED FUNCTION.

def remove_duplicates(list1):
    unique = [] # we want to store unique values in this list, so we initialize it as empty list.

    for i in list1:
        if i not in unique:
            unique.append(i)
    return unique # we want final result after loop finishes complletely thats why return is outside loop.

list1 = [1, 2, 2, 4, 4, 3]
result = remove_duplicates(list1)
print("Updated list after op.", result)  # OUTPUT: Updated list after op. [1, 2, 4, 3]




# 7. (V.IMP) COUNT EVEN AND ODD NUMBERS IN A LIST.

def count_even_odd(list2):
    even_count = 0
    odd_count = 0

    if type(list2) == list: # to check if input is list or not, if not return error message.
        for i in list2:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    else:
        print("Error: Input is not a list.")
    
    return even_count, odd_count

list2 = [21, 42, 63, 84, 105, 126]
even_count, odd_count = count_even_odd(list2)

print("Total even numbers in the list:", even_count)  # OUTPUT: Even count: 3
print("Total odd numbers in the list:", odd_count)    # OUTPUT: Odd count: 3




# 8. (IMP) FIND SUM OF NEGATIVE, POSITIVE EVEN & POSITIVE ODD NUMBERS IN A LIST.

# TAKING LIST AS INPUT FROM USER.

list3 = [] # we want to store user input in this list, so we initialize it as empty list.

n = int(input("Enter total no. of elements: "))
for i in range(n):
    num = int(input("Enter number: ")) 
    list3.append(num)


print("List of numbers:", list3) # this is just to check if we have taken input correctly or not, we can remove this line later if we want.

neg_sum = 0
pos_even_sum = 0
odd_sum = 0

for num in list3: # take each number from list one by one and check if it is negative, positive even or positive odd and add it to respective sum variable.
    
    if num < 0:
        neg_sum += num
    else: 
        if num % 2 == 0:
            pos_even_sum += num
        else:
            odd_sum += num

print("Sum of negative numbers:", neg_sum) 
print("Sum of positive even numbers:", pos_even_sum)
print("Sum of positive odd numbers:", odd_sum)

'''
OUTPUT: Enter total no. of elements: 6
List of numbers: [-1, -2, 3, 5, 2, 6]
Enter number: -1
Enter number: -2
Enter number: 3
Enter number: 5
Enter number: 2
Enter number: 6
Sum of negative numbers: -3
Sum of positive even numbers: 8
Sum of positive odd numbers: 8
'''

# list3 = list(map(int, input("Enter number separated by space:"). split())) # this is another way to take list input from user, here we take input as string and then split it into list of strings and then convert each string to integer using map() function.


