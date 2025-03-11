import pandas as pd
import matplotlib.pyplot as plt


# Cargar el dataset
df = pd.read_csv('housing.csv')

# Calcular estadísticas para median_house_value
stats_dict = {
    'Media': df['median_house_value'].mean(),
    'Mediana': df['median_house_value'].median(),
    'Moda': df['median_house_value'].mode()[0],
    'Rango': df['median_house_value'].max() - df['median_house_value'].min(),
    'Varianza': df['median_house_value'].var(),
    'Desviación Estándar': df['median_house_value'].std()
}

# Crear tabla de estadísticas
print("\nEstadísticas de median_house_value:")
stats_df = pd.DataFrame.from_dict(stats_dict, orient='index', columns=['Valor'])
print(stats_df.to_string())

# Crear tabla de frecuencias
bins = 10
freq_table = pd.cut(df['median_house_value'], bins=bins).value_counts().sort_index()
print("\nTabla de Frecuencias:")
print(freq_table)

# Crear histogramas comparativos
plt.figure(figsize=(15, 5))

# plt.subplot(131) significa:
# - 1: número de filas en la cuadrícula
# - 3: número de columnas en la cuadrícula
# - 1: posición del subplot actual (primer lugar)
plt.subplot(131)  # Esto crea una cuadrícula de 1x3 y selecciona el primer panel
plt.scatter(df['total_bedrooms'], df['median_house_value'], alpha=0.5)
plt.xlabel('Total Bedrooms')
plt.ylabel('Median House Value')
plt.title('House Value vs Bedrooms')

# El segundo subplot (132) selecciona la segunda posición
plt.subplot(132)  # Selecciona el segundo panel de la cuadrícula 1x3
plt.scatter(df['population'], df['median_house_value'], alpha=0.5)
plt.xlabel('Population')
plt.ylabel('Median House Value')
plt.title('House Value vs Population')

# El tercer subplot (133) selecciona la tercera posición
plt.subplot(133)  # Selecciona el tercer panel de la cuadrícula 1x3
plt.hist(df['median_house_value'], bins=30)
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Distribution of House Values')

plt.tight_layout()
plt.show()
