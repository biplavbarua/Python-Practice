import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(arr)

#1. Replace the diagonal elements with 0.
np.fill_diagonal(arr,0)
print(arr)

#2. Create a new matrix where every element greater than 10 is replaced by 100.
arr[arr > 10] = 100
print(arr)
