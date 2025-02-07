import pandas as pd

data = {
        'Department':['HR','IT','HR','Finance','Marketing'],
        'Employee': ['John', 'Jas', 'Karan', 'Preet', 'Eve'],
        'Salary': [50000, 60000, 55000, 52000, 70000]
        }

df = pd.DataFrame(data)

#Group by Department and find average salary

result = df.groupby('Department')['Salary'].mean()
print(result)
