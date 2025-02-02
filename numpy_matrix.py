import numpy as np

#Step 1: Create a 4x4 matrix with values from 1 to 16
matrix = np.arange(1,17).reshape(4,4)
print("Original 4x4 Matrix: ")
print(matrix)

#Step 2: Reshape the matrix into 2x8
reshaped_matrix = matrix.reshape(2,8)
print("\nReshaped 2x8 Matrix: ")
print(reshaped_matrix)

#Step 3: Perform operations on the original 4x4 matrix
#Transpose
transpose_matrix = matrix.T
print("\nTranspose of the Matrix: ")
print(transpose_matrix)

#Sum of each row
row_sums = np.sum(matrix, axis=1)
print("\nSum of each row")
print(row_sums)
