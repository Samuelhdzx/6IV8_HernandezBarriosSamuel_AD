import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Definir la ruta de la carpeta donde se guardarán las gráficas
carpeta_graficos = 'graficos_analisis'
os.makedirs(carpeta_graficos, exist_ok=True)

# Carga de información de archivos
info_catalogo = pd.read_csv('../Excels/Catalogo_sucursal.csv')
info_proyecto = pd.read_csv('../Excels/proyecto1.csv')

# Unificación de conjuntos de datos
informacion_consolidada = info_proyecto.merge(info_catalogo, on='id_sucursal')

# Cálculo de ingresos totales
ingresos_globales = informacion_consolidada['ventas_tot'].sum()
print(f"Ingresos totales del establecimiento: ${ingresos_globales:.2f}")

# Análisis de estatus de adeudo
distribucion_adeudo = informacion_consolidada['B_adeudo'].value_counts()
proporcion_adeudo = informacion_consolidada['B_adeudo'].value_counts(normalize=True) * 100

print(distribucion_adeudo)
print(proporcion_adeudo.round(2))

# Estimación de pasivos
pasivos_totales = informacion_consolidada['adeudo_actual'].sum()
print(f"Pasivos totales de clientes: ${pasivos_totales:.2f}")

# Evaluación de rendimiento económico
beneficio_neto = ingresos_globales - pasivos_totales
porcentaje_rendimiento = (beneficio_neto / ingresos_globales) * 100
print(f"Porcentaje de rendimiento del establecimiento: {porcentaje_rendimiento:.2f}%")

# Visualización de ventas totales respecto del tiempo
plt.figure(figsize=(12,6))
ingresos_periodicos = informacion_consolidada.groupby('B_mes')['ventas_tot'].sum()
ingresos_periodicos.plot(kind='bar', color='coral')
plt.title("Ventas totales respecto del tiempo")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, 'ventas_totales.png'))
plt.close()

# Análisis de desviación estándar de pagos
plt.figure(figsize=(12,6))
varianza_pagos_periodo = informacion_consolidada.groupby('B_mes')['pagos_tot'].std()
varianza_pagos_periodo.plot(marker='o', linestyle='-', color='teal')
plt.title("Desviación estándar de pagos respecto del tiempo")
plt.xlabel("Mes")
plt.ylabel("Desviación estándar")
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, 'desviacion_pagos.png'))
plt.close()

# Distribución de ventas por sucursal
plt.figure(figsize=(8,8))
ingresos_punto_venta = informacion_consolidada.groupby('suc')['ventas_tot'].sum()
ingresos_punto_venta.plot(kind='pie', autopct='%1.1f%%', cmap='Set2')
plt.title("Ventas por sucursal")
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, 'ventas_sucursal.png'))
plt.close()

# Comparativo de deuda total vs margen de utilidad por sucursal
pasivos_punto_venta = informacion_consolidada.groupby('suc')['adeudo_actual'].sum()
beneficios_punto_venta = ingresos_punto_venta - pasivos_punto_venta
indices = np.arange(len(ingresos_punto_venta))
ancho_barra = 0.35

plt.figure(figsize=(12,6))
plt.bar(indices - ancho_barra/2, pasivos_punto_venta, ancho_barra, color='mediumorchid', label='Deuda total')
plt.bar(indices + ancho_barra/2, beneficios_punto_venta, ancho_barra, color='mediumseagreen', label='Margen utilidad')
plt.xlabel('Sucursal')
plt.ylabel('Monto')
plt.title('Deuda total vs Margen de utilidad por sucursal')
plt.xticks(indices, ingresos_punto_venta.index)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, 'deuda_vs_margen.png'))
plt.close()

print(f"Gráficos guardados en la carpeta: {carpeta_graficos}")