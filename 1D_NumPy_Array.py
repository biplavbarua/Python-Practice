import numpy as np

#Step 1: Create a 1D array with 15 random integers between 50 and 100.
array = np.random.randint(50, 101, 15)
print("1D NumPy Array: ")
print(array)

#Step 2: Perform statistical operations
#Mean, Median, and Standard Deviation
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)

print("\n Mean of the array: ", mean)
print("\nMedian of the array", median)
print("Standard Deviation of the array: ", std_dev)

#count of elements greater than 75
greater_than_75 = np.sum(array > 75)
print("\nNumber of elements greater than 75: ", greater_than_75)

#Indices of elements less than 60
indices_less_than_60 = np.where(array < 60)[0]
print("\nIndices of the elements less than 60: ", indices_less_than_60)
