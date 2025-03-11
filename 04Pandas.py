import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('housing.csv')

# Display first and last rows
print(df.head())
print(df.tail())

# Display row at index 7
print(df.iloc[7])

# Display ocean_proximity column
print(df["ocean_proximity"])

# Calculate mean of total_bedrooms
mean_bedrooms = df['total_bedrooms'].mean()
print('La media de total room es', mean_bedrooms)

# Calculate median of total_bedrooms
median_bedrooms = df['total_bedrooms'].median()
print('La mediana de total room es', median_bedrooms)

# Calculate sum of population
total_population = df['population'].sum()
print('El total de población es', total_population)

# Filter rows where ocean_proximity is 'ISLAND'
island_filter = df[df['ocean_proximity'] == 'ISLAND']
print(island_filter)

plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])

plt.xlabel('Proximidad al Océano')
plt.ylabel('Precio')

plt.title('Relación entre Proximidad al Océano y Precio')
plt.show()