import pandas as pd 

#Hacer un 
inicio = int(input("Introduce el año de ventas inicial: "))
fin = int(input("Introduce el año de ventas final: "))

ventas = {}

for i in range (inicio, fin+1):
    ventas[i] = float(input("Introduce la venta de año " + str(i) + ": "))

ventas = pd.Series(ventas)
print('Ventas \n ', ventas)
print('Ventas con descuento \n ', ventas*0.9)