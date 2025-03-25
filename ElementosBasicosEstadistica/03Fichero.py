import pandas as pd

def resumen_cotizacion(fichero):
    df = pd.read_csv(fichero, sep=';' , decimal=',' , thousands='.', 
    index_col=0)
    return pd.DataFrame([df.mean(), df.std(), df.min(), df.max()], index=['Media', 'Desviacion tipica', 'Minimo', 'Maximo'])

resumen_cotizacion('cotizacion.csv')
print(resumen_cotizacion('cotizacion.csv'))
