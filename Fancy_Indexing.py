import numpy as np

arr = np.array([10,20,30,40,50])
indices = [0,2,4]

#1. Extract elements from arr using indices
print(arr[indices])

#2. Change the elements at indices [1,3]
arr[[1,3]] = 99
print(arr)
