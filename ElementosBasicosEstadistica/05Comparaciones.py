import numpy as np 
import matplotlib.pyplot as plt

#crear una semilla random reproductiva
np.random.seed(0)

#vamos a buscar los parametros para una distribucion media
media=0
#desviaciones estandar
sigma1=1
sigma2=2
sigma3=3

#el numero de muestras para el analisis 
n_muestras = 1000 

#vamos a generar los datos de las distribuciones normales
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

plt.figure(figsize=(10, 6))

#vamos a crear un histograma para cada distribucion
plt.hist(data1, bins=30, color='skyblue', density=True, alpha=0.5, label='data1')
plt.hist(data2, bins=30, color='red', density=True, alpha=0.5, label='data2')
plt.hist(data3, bins=30, color='green', density=True, alpha=0.5, label='data3')

plt.title('Comparaciones de Distribuciones Normales con una semilla en random')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.axhline(y=0.5, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x=0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.show()