import pandas as pd
import matplotlib.pyplot as plt


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

# Primer histograma
plt.subplot(131)
plt.hist(df['median_house_value'], bins=30, alpha=0.5, label='House Value')
plt.hist(df['total_bedrooms'], bins=30, alpha=0.5, label='Total Bedrooms')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('House Value vs Bedrooms')
plt.legend()

# Segundo histograma
plt.subplot(132)
plt.hist(df['median_house_value'], bins=30, alpha=0.5, label='House Value')
plt.hist(df['population'], bins=30, alpha=0.5, label='Population')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('House Value vs Population')
plt.legend()

# Tercer histograma (solo median_house_value)
plt.subplot(133)
plt.hist(df['median_house_value'], bins=30, color='skyblue')
plt.xlabel('Median House Value')
plt.ylabel('Frecuencia')
plt.title('Distribution of House Values')

plt.tight_layout()
plt.show()
