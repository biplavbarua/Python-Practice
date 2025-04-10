import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('Iris')
print(iris.head())

#Visualization to check skewness using histogram
#Plot histograms to visualize skewness
iris.hist(bins=20, color='red', grid=False, edgecolor="black")
plt.title("Histogram of Numeric Features in Iris Dataset")
plt.show()
#IQR is the better choice for the datasets whenever there is skewness in the data (positive/negative)

#Compute Q1 (25th percentile) and Q3 (75th percentile)
Q1 = numeric_cols.quantile(0.25)
Q2 = numeric_cols.quantile(0.75)
IQR = Q3 - Q1

#Define outliers as values outside 1.5*IQR range
outliers = ((numeric_cols < (Q1 - 1.5 * IQR)) | (numberic_cols > (Q3 + 1.5 * IQR)))
outliers_counts = outliers.sum()

#Print rows containing outliers
print ("Outliers Detected: \n", iris[outliers.any(axis=1)])

#Count total outlier rows
total = outliers.any(axis=0).sum()

#Print results
print("Outliers count per column: ", outlier_counts)
print("\nTotal No. of Rows containing outliers: ", total)
