import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Sample data
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'Value1': np.random.randn(100),
    'Value2': np.random.randn(100) * 10 + 50,
    'Time': pd.date_range(start='2025-04-04', periods=100,
                           freq='D')
    })

#randn generates numbers having Mean = 0 and Standard Deviation = 1
#uniform distribution
#rand generates random numbers between - and 1
#normal distribution (bell shaped curve -3 to 3, centered around 0
#freq = D, W, M

print(data)
# Set the style
sns.set(style="whitegrid")

#1. Line Plot
plt.figure(figsize=(8, 4))
sns.lineplot(data=data, x='Time', y='Value1')
sns.lineplot(data=data, x='Time', y='Value2', color='r')
plt.title('Line Plot Example')
plt.show()

#2. Bar Plot
plt.figure(figsize=(8, 4))
sns.barplot(data=data, x='Category', y='Value2', errorbar=None)
plt.title('Bar Plot Example')
plt.show()
#The errorbar parameter controls
#(representing variability are displayed on the bars.)

#3. Scatter Plot
plt.figure(figsize=(8, 4))
sns.scatterplot(data=data, x='Value1', y='Value2', hue='Category', style='Category', s=100)
plt.title('Scatter Plot Example')
plt.show()

palette = {'A':'red', 'B':'blue', 'C':'orange', 'D':'yellow'}
markers = {'A':'H', 'B':'P', 'C':'D', 'D':'*'}
sns.scatterplot(data=data, x='Value1', y='Value2', hue='Category', style='Category',
                palette = palette,
                markers = markers, s=100)
plt.title('Scatter Plot Example')
plt.xlabel('Value 1 (X-Axis)')
plt.ylabel('Value 2 (Y-Axis)')
plt.show()

#4. Heatmap
plt.figure(figsize=(6, 4))
corr = data[['Value1', 'Value2']].corr()
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0)
plt.title('Heatmap Example')
plt.show()
