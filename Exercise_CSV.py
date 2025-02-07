import pandas as pd

#Sample Dataset
df = pd.DataFrame({'Name':['Aman', 'Bhumika', 'Deep'],
                   'Marks': [85, 90, 78]})

#Save as CSV
df.to_csv("output.csv", index=True)

#Save as Excel
df.to_excel("output.xlsx", index=True)
