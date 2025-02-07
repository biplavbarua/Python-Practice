import pandas as pd

data = {
        'Food':['Pizza','Samosa','Pasta','Momos','Sushi'],
        'Cuisine': ['Italian','Indian','French','Tibetian','Chinese'],
        'Price': [1000, 100, 500, 150, 750]
        }

df = pd.DataFrame(data)

#Group by Food and Average Price

result = df.groupby('Food')['Price'].mean()
print(result)
