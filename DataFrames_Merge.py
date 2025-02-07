import pandas as pd

df1 = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Name': ['Alice','Bob','Charlie'],
    'Dept': ['HR','IT','Finance']
    })

df2 = pd.DataFrame({
    'EmployeeID': [101, 102, 104],
    'Salary': [50000, 60000, 55000]
    })

df3 = pd.DataFrame({
    'EmployeeID': [101, 102, 105],
    'Age': [25, 30, 35]
    })

#Merge both DataFrames on EmployeeID

merged_df = pd.merge(df1, df2, on="EmployeeID",how="left")
print(merged_df)

#Merge all DataFrames

new_merged_df = pd.merge(merged_df, df3, on="EmployeeID", how="left")
print(new_merged_df)

#Cross-Product
mergednew_df = merged_df.merge(df3, how="cross")
print(mergednew_df)
