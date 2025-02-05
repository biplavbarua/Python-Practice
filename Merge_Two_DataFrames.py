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

#Merge both DataFrames on EmployeeID

merged_df = pd.merge(df1, df2, on="EmployeeID",how="left")
print(merged_df)
