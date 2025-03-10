import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.mean(), notas.std(), notas.min(), notas.max()], index=['Media', 'Desviacion tipica', 'Minimo', 'Maximo'])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending=False)

notas = {'Juan': 9, 'Jaunita': 7, 'Pedro': 6.6, 'Fabian': 8.5, 'Maximiliano': 7.5, 'Sandra': 9.8, 'Rosario': 9}

print(estadistica_notas(notas))
print (aprobados(notas))