import numpy as np

arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr)

#1. Extract the subarray consisting of the first 2 rows and first 2 coloumns.
print(arr[:2, :2])

#2. Extract all elements in the last row
print(arr[-1])

#3. Replace the second coloumn with all zeros
arr[:, 1] = 0
print(arr)
