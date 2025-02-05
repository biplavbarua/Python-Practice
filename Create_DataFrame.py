import pandas as pd

#Creating and Exploring a DataFrame
#Step 1: Create the DataFrame

data = {
    'Name': ['John','Alice','Bob','Emma'],
    'Age': [25, 23, 24, 22],
    'Gender': ['Male','Female','Male','Female'],
    'Marks': [85, 90, 75, 95]
}

df = pd.DataFrame(data)
print(df)

#Step 2: Display the first two rows of the DataFrame

print("\nFirst two rows: ")
print(df.head(2))

#Step 3: Get a list of all column names in the DataFrame

print("\nColumn names: ")
print(df.columns.tolist())

#Step 4: Find the shape (number of rows and columns) of the DataFrame

print("\nShape of DataFrame")
print(df.shape)
