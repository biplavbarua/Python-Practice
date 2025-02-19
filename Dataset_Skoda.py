import pandas as pd

#Load the CSV File
df = pd.read_csv(r'/Users/biplavbarua/Downloads/skoda.csv')
#r is the raw string

#Display the first few rows of the dataset to ensure it's loaded correctly
print(df.head(19))

#For column names and data type information
print("Column names and data types: ")
print(df.info())

#Describe function gives mean, median, min, max, 25%, 50%, 75%
print(df.describe())

#Summary Statistics: Mean, Median, and Standard Deviation of the 'Price'
print("\nSummary statistics for 'price' column:")
print(f"Mean: {df['price'].mean().round(2)}")
print(f"Median: {df['price'].median().round(2)}")
print(f"Standard Deviation: {df['price'].std().round(2)}")


#Filtering: Filter cars with 'manual' transmission and count them
manual_cars = df[df['transmission'] == 'Manual']
print(f"\nNumber of cars with 'manual' transmission: {manual_cars.shape[0]}")
#shape[0] is written for rows here

automatic_cars = df[df['transmission'] == 'Automatic']
print(f"\nNumber of cars with 'automatic' transmission: {automatic_cars.shape[0]}")


#Categorical Data Analysis: Unique Fuel Types
unique_fuel_types = df['fuelType'].unique()
print(f"\nUnique fuel types: {unique_fuel_types}")

#Handling Missing Data: Check for missing values
missing_data = df.isnull().sum()
print(f"\nMissing data in each column: \n{missing_data}")

#df.null() creates a DataFrame of the same shape as df
#where each entry is either True or False
#isnull().sum() will give you total number of missing values for each column.


#Data Aggregation: Average price by fuel type, Model, Transmission
average_price_by_fuel = df.groupby('fuelType')['price'].mean()
average_price_by_model = df.groupby('model')['price'].mean()
average_price_by_transmission = df.groupby('transmission')['price'].mean()
print(f"\nAverage price by fuel type: \n{average_price_by_fuel}")
print(f"\nAverage price by model type: \n{average_price_by_model}")
print(f"\nAverage price by transmission type: \n{average_price_by_transmission}")

#Data Sorting Sort by 'price' in descending order
sorted_by_price = df.sort_values('price', ascending=False)
print(f"\nHighest priced car: \n{sorted_by_price.head(10)}")
