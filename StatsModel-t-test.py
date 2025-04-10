from scipy.stats import ttest_ind
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Load the dataset
df=pd.read_csv(r"/Users/biplavbarua/Downloads/WorldBank.csv", encoding='latin1')

#Select GDP data for two countries
india_gdp = df[df["Country Name"] == "India"] ["GDP (USED)"].dropna()
use_gdp = df[df["Country Name"] == "United States"] ["GDP (USD)"].dropna()

#Ensure there is enough data for the test
if len(india_gdp) > 1 and len(usa_gdp) > 1:
#Perform Welch's T-test (default: equal_var=False for unequal variance)
    t_stat, p_value = ttest_ind(india_gdp, usa_gdp, equal_var=False)

    print(f"T-statistics: {t_stat: 4f}")
    print(f"P-value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: There is significant difference in")
    else:
        print("Fail to reject the nul hypothesis: No significant difference in")
else:
    print("Not enough data for T-test.")
