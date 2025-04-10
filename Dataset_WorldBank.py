import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the Dataset
file_path = (r'/Users/biplavbarua/Downloads/WorldBank.csv')
df = pd.read_csv(file_path)

#Display dataset info
num_rows, num_columns = df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")
print(df.head())

#Define correct column names
country_col = "Country Name"
year_col = "Year"
gdp_col = "GDP (USD)"

#Line Chart: GDP Trends Over Time
country = "India"
df_country = df[df[country_col] == country]

if year_col in df.columns and gdp_col in df.columns:
    df_country = df_country.sort_values(year_col)  
    plt.figure(figsize=(10, 5))
    plt.plot(df_country[year_col], df_country[gdp_col], marker='o', linestyle='-', color='b')
    plt.xlabel(year_col)
    plt.ylabel(gdp_col)
    plt.title(f"GDP Trends for {country} Over Time")
    plt.grid(True)
    plt.show()
else:
    print(f"Columns '{year_col}' and '{gdp_col}' not found. Check column names.")

# ----- Bar Chart: GDP Comparison for Multiple Countries -----
year = 2018  # Change to desired year
df_year = df[df[year_col] == year]

top_countries = df_year.sort_values(gdp_col, ascending=False).head(10)  # Top 10 countries
if not top_countries.empty:
    plt.figure(figsize=(12, 6))
    plt.bar(top_countries[country_col], top_countries[gdp_col], color='g')
    plt.xlabel("Country")
    plt.ylabel("GDP (USD)")
    plt.title(f" Top 10 Countries by GDP in {year}")
    plt.xticks(rotation=45)
    plt.show()
# ----- Histogram - Distribution of GDP -----
plt.figure(figsize=(10, 5))
plt.hist(df[gdp_col].dropna(), bins=10, color='c', edgecolor='black')  # Drop NaN values
plt.xlabel("GDP (USD)")
plt.ylabel("Frequency")
plt.title("Histogram of GDP Distribution")
plt.grid()
plt.show()

# ------ Scatter plot - GDP vs population

plt.figure(figsize=(10, 6))
plt.scatter(df['Population'], df['GDP (USD)'], color='blue', alpha=0.7)
    
plt.title('GDP (USD) vs Population', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('GDP (USD)', fontsize=14)
    
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#KDE: Kernal Density estimation (used for easy interpretation)
plt.title("GDP Distribution (Seaborn)")
plt.xlabel("GDP (USD)")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
plt.show()

#Difference: The Seabrn histogram automatically includes a Kernel Density Estimation (KDE)
#curve, making it easier to interpret.


#How does GDP (in USD) relate to life expectancy at birth across different regions?
#Create a scatter plot using Seaborn to visualize this relationship

plt.figure(figsize = (8, 6))
sns.scatterplot(x=df["GDP (USD)"], y=df["Life expectancy at birth (years)"],  hur=df["Region"], alpha=0.8, legend=False)
plt.title("GDP vs Life Expectancy (Seaborn)")
plt.ylabel("Life Expectancy")
plt.xscale("log")

plt.show()

#Box Plot: GDP Distribution by Region
plt.figure(figsize=(8,5))
sns.boxplot(x="Region", y="GDP (USD)", hue="Region", data=df)
plt.title("GDP Distribution by Region (Box Plot)")
plt.xlabel("Region")
plt.ylabel("GDP (USD)")
#plt.xscale("log")
#plt.yscale("log")
plt.xticks(rotation=30)
plt.show()

#Heatmap: Correlation Matrix of Nuerical Variables
plt.figure(figsize=(8,5))
corr_matrix = df.select_dtypes(imclude = ['number']).corr()
sns.heatmap()
