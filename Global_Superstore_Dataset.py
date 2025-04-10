import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/biplavbarua/Downloads/Global_Superstore(CSV).csv")
print(df.head())

missing_data = df.isnull().sum()
print(f"\nMissing data in each column: \n{missing_data}")

print(df.shape)
print(df.info())
print(df.describe())
print(df.columns.tolist())
#checking for duplicate values
print(df.nunique())

#Bar Plot
quality_counts = df['Country'].value_counts()

plt.figure(figsize=(10, 8))
plt.bar(quality_counts.index, quality_counts, color='green')
plt.title('Country')
plt.xlabel('Quantity')
plt.ylabel('Count')
plt.show()
