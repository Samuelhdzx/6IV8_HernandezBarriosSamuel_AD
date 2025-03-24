import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Leer datos desde archivos CSV
df_catalogo = pd.read_csv('Catalogo_sucursal.csv')
df_proyecto = pd.read_csv('Proyecto1.csv')

# Realizar un merge entre df_proyecto y df_catalogo utilizando la columna de sucursales
df_merged = pd.merge(df_proyecto, df_catalogo, left_on='suc', right_on='suc')

# Asegúrate de que los nombres de las columnas coincidan con los de tus archivos CSV
ventas = df_merged['ventas_tot'].tolist()
tiempo = df_merged['fec_ini_cdto'].tolist()
adeudos = df_merged['B_adeudo'].tolist()
sucursales = df_merged['suc'].tolist()

ventas_por_sucursal = df_merged.groupby('suc')['ventas_tot'].sum().tolist()
deudas_por_sucursal = df_merged.groupby('suc')['B_adeudo'].sum().tolist()
utilidad_por_sucursal = [v - d for v, d in zip(ventas_por_sucursal, deudas_por_sucursal)]

# 1. Ventas totales del comercio
ventas_totales = sum(ventas)
print(f"Ventas totales del comercio: {ventas_totales}")

# 2. Socios con y sin adeudo
socios_con_adeudo = sum(1 for adeudo in adeudos if adeudo > 0)
socios_sin_adeudo = len(adeudos) - socios_con_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / len(adeudos)) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / len(adeudos)) * 100
print(f"Socios con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.2f}%)")
print(f"Socios sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.2f}%)")

# 3. Gráfica de ventas totales respecto del tiempo
plt.figure(figsize=(10, 6))
plt.bar(tiempo, ventas, color='blue')
plt.title('Ventas Totales Respecto del Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Ventas')
plt.show()

# 4. Gráfica de la desviación estándar de los pagos realizados respecto del tiempo
desviacion_estandar = np.std(ventas)
plt.figure(figsize=(10, 6))
plt.bar(tiempo, [desviacion_estandar] * len(tiempo), color='orange')
plt.title('Desviación Estándar de los Pagos Realizados Respecto del Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Desviación Estándar')
plt.show()

# 5. Deuda total de los clientes
deuda_total = sum(adeudos)
print(f"Deuda total de los clientes: {deuda_total}")

# 6. Porcentaje de utilidad del comercio
utilidad_total = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad_total / ventas_totales) * 100
print(f"Porcentaje de utilidad del comercio: {porcentaje_utilidad:.2f}%")

# 7. Gráfico circular de ventas por sucursal
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_sucursal, labels=sucursales, autopct='%1.1f%%', startangle=140)
plt.title('Ventas por Sucursal')
plt.show()

# 8. Gráfico de deudas totales por cada sucursal respecto del margen de utilidad de cada sucursal
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Sucursales')
ax1.set_ylabel('Deudas Totales', color=color)
ax1.bar(sucursales, deudas_por_sucursal, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Margen de Utilidad', color=color)
ax2.plot(sucursales, utilidad_por_sucursal, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Deudas Totales por Sucursal vs Margen de Utilidad')
plt.show()