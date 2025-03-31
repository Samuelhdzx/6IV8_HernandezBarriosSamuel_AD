# Calcularemos la distancia entre todos los pares de puntos y determinaremos cuales están mas cercanos
# euclidiana, manhattan y chebyshev
import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos = {
    'punto1': (2, 3),
    'punto2': (5, 4),
    'punto3': (1, 1),
    'punto4': (5, 7),
    'punto5': (3, 5),
    'punto6': (8, 2),
    'punto7': (2, 1),
    'punto8': (3, 3),
}

df_puntos = pd.DataFrame.from_dict(puntos).T
df_puntos.columns = ['x', 'y']
print('Coordenadas de los puntos:')
print(df_puntos)

def calcular_distancias(puntos):
    distancia = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    # Calcula las distancias
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i != k:
                distancia.loc[i,k] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[k])
    return distancia

def calcular_distancias_manhattan(puntos):
    distancia = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    # Calcula las distancias
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i != k:
                distancia.loc[i,k] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[k])
    return distancia

def calcular_distancias_chebyshev(puntos):
    distancia = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    # Calcula las distancias
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i != k:
                distancia.loc[i,k] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[k])
    return distancia

# Calculamos las distancias con los tres métodos
distancias = calcular_distancias(puntos)
distancias_manhattan = calcular_distancias_manhattan(puntos)
distancias_chebyshev = calcular_distancias_chebyshev(puntos)

# Para distancia euclidiana
valor_maximo = distancias.values.max()
punto1, punto2 = distancias.stack().idxmax()
print('Tabla de distancias:')
print(distancias)
print('Distancia máxima:', valor_maximo)
print('Entre el punto', punto1, 'y el punto', punto2) # Distancia Euclidiana

# Otra manera
max_value = distancias.max().max()
# Obtener la columna que contiene el valor máximo
col_max = distancias.max().idxmax()
# Obtener el índice (fila) que contiene el valor máximo
id_max = distancias[col_max].idxmax()

print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")

# Para distancia Manhattan
valor_maximo_manhattan = distancias_manhattan.values.max()
punto1_m, punto2_m = distancias_manhattan.stack().idxmax()
print('\nTabla de distancias Manhattan:')
print(distancias_manhattan)
print('Distancia Manhattan máxima:', valor_maximo_manhattan)
print('Entre el punto', punto1_m, 'y el punto', punto2_m)

# Para distancia Chebyshev
valor_maximo_chebyshev = distancias_chebyshev.values.max()
punto1_c, punto2_c = distancias_chebyshev.stack().idxmax()
print('\nTabla de distancias Chebyshev:')
print(distancias_chebyshev)
print('Distancia Chebyshev máxima:', valor_maximo_chebyshev)
print('Entre el punto', punto1_c, 'y el punto', punto2_c)