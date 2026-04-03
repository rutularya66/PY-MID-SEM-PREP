# 9. (AVG) TRANSPOSE OF A 2- D MATRIX:

# EX. A = [[1,2], [3,4]]
# TRANSPOSE OF A = [[1,3], [2,4]]

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the elements of the matrix:")

for i in range(rows):
    row = list(map(int, input().split()))  # take input for each row as space separated values and convert them to integers

    matrix.append(row)

# Now we have the original matrix, we will create a new matrix for the transpose

transpose = []

for j in range(cols): 
    new_row = []

    for i in range(rows):
        new_row.append(matrix[i][j])  # append the element at position (i,j) of original matrix to new_row
    transpose.append(new_row)  # append the new_row to transpose matrix

print("Transpose of the matrix:")

for r in transpose:
    print(r)  # print each row of the transpose matrix


# 2 loops simply means we will take each column of original matrix and make it a row in the transpose matrix, we will do this for all columns of original matrix.
'''
Output: Enter number of rows: 2
Enter number of columns: 2
Enter the elements of the matrix:
2 3
4 5
Transpose of the matrix:
[2, 4]
[3, 5]
'''

# dry-run :
# original matrix: [[1,2], [3,4]]
# transpose = []
# i = 0, j = 0: new_row = [1] (append element at position (0,0) of original matrix)
# i = 1, j = 0: new_row = [1,3] (append element at position (1,0) of original matrix)
# transpose = [[1,3]]
# i = 0, j = 1: new_row = [2] (append element at position (0,1) of original matrix)
# i = 1, j = 1: new_row = [2,4] (append element at position (1,1) of original matrix)
# transpose = [[1,3], [2,4]]


