import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

#1. Create a new array containing only the even numbers from arr.
even_numbers = arr[arr % 2 == 0]
print(even_numbers)

#2. Set all odd numbers in the array to -1.
arr[arr % 2 != 0] = -1
print(arr)
