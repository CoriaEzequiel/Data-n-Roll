#manejar y modificar datos de manera eficiente
#perfecto para datos tabulares.
#analisis de datos, ciencia de datos, inteligencia de negocios 
#y cualquier campo que requiera manipular y analizar grandes cantidades de datos.
import pandas as pd

serie = pd.Series([1,2,3,4,5,6])# "una columna"
print(serie)



datos={
    'nombre':["Ana","Clara","Martina"],
    'edad':[25,29,33]
}
#DataFrame => estructura de datos que tiene filas y columnas

df = pd.DataFrame(datos) #entrego diccionario, listas, etc.
print(df)
