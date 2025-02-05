import numpy as np

arr = np.array([5,10,15,20,25])
print(arr)

#1. Multiply all elements by 2
print(arr*2)

#2. Replace all values greater than 10 with 99
arr[arr > 10] = 99
print(arr)

#3. Add 50 to every element in the array
arr += 50
print(arr)
