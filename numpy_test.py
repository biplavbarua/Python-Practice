import numpy as np

#Step 1: Create the arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 6, 8, 10])

#Step 2: Perform element-wise operations
#Addition
array_sum = array1 + array2
print("Element-wise addition of array1 and array2: ")
print(array_sum)

#Multiplication
array_product = array1 * array2
print("\nElement-wise multiplication of array1 and array2: ")
print(array_product)

#Square of each element in array1
array1_square = array1 ** 2
print("\nSquare of each element in array1: ")
print(array1_square)
