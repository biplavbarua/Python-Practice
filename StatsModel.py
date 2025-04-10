#pip install statsmodels
from statsmodels.stats.weightstats import ztest

#The ztest function from statsmodels is used
#for performing a Z-test to compare the means of two independent samples. It tests
#whether the means of two populations are significantly different based on the sample data.

#Select GDP data for two countries
india_gdp = df[df["Country Name"] == "India"] ["GDP (USED)"].dropna()
use_gdp = df[df["Country Name"] == "United States"] ["GDP (USD)"].dropna()

#Perform Z-test
z_stat, p_value = ztest(india_gdp, usa_gdp)

print(f"Z-statistic: (z_stat: )")
