#pip install matplotlib in command prompt
import matplotlib.pyplot as plt

fuel_type_counts = df['fuelType'].value_counts()
fuel_type_counts.plot(kind='bar', title="Count of Cars by Fuel Type")
plt.ylabel("Count")

plt.show()
