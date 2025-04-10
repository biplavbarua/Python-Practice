import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset with proper encoding
df = pd.read_csv(r"/Users/biplavbarua/Downloads/german.csv", encoding = 'ISO-8859-1')

#Display the first five rows
print("First 5 rows of the dataset: ")
print(df.head())

#Number of rows and columns
print("\nShape of the dataset: ", df.shape)

#Unique values in "Credit history"
print("\nUnique values in 'Credit history':", df["Credit history"].unique())
#Count occurrences in "Default status"

#Count occurances in "Default status"
print("\nCount of 'Default status':")
print(df["Default status"].value_counts())



#Maximum and Minimum Age
print("\nMaximum Age:", df["Age in Years"].max())
print("Minimum Age:", df["Age in Years"].min())


#Standard deviation of "Installment rate in percentage in disposable income"
print("\nStandard Deviation of Installment Rate:", df["Installment rate in percentage of disposable income"])

#Normalize "Credit amount" using min-max scaling
df["Credit amount normalized"] = (df["Credit amount"] - df["Credit amount"].min() / (df["Credit amount"].max() - df["Credit amount"].min()))
print("\nNormalized 'Credit amount' column:")
print(df[["Credit amount","Credit amount normalized"]].head(10))

#Extract records where "Duration in month" > 24
filtered_data = df[df["Duration in month"] > 24]
print(filtered_data.head())
