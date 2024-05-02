# Importamos las librerias Pandas y Numpy. Son bastantes populares y se utilizan
# Para la manipulación y análisis de datos

import pandas as pd
import numpy as np

# Se carga el archivo housing.csv en un Dataframe de pandas al que llamaremos df
# Para ello usaremos la función read_csv()

df = pd.read_csv('housing.csv')

# En este caso como sabemos que el modelo puede tener alguna errata, vamos a
# Proceder a limpiar entradas que no tengan mucho sentido
# Eliminameros todas las filas si en algunos de los siguientes elementos son negativos
# 0   longitude           
# 1   latitude            
# 2   housing_median_age  
# 3   total_rooms -> no puede ser negativas         
# 4   total_bedrooms  -> no puede ser negativas    
# 5   population  -> no puede ser negativas 
# 6   households  -> no puede ser negativas      
# 7   median_income  -> no puede ser negativas 
# 8   median_house_value -> no puede ser negativas 
# 9   ocean_proximity

# Mostramos por pantalla el total de entradas de nuestro dataset usando la función shape()

print("Número de entradas antes de la limpieza:", df.shape[0])

# Creamos una lista que contiene los nombres de las columnas que queremos verificar

cols_to_check = ['total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

# Iteramos por todas las columnas y nos quedamos sólo con aquellas cuyos valores
# Sean mayores que cero

for col in cols_to_check:
    df = df[df[col] >= 0]

# Finalmente mostramos de nuevo por pantalla el número de entradas tras la limpieza

print("Número de entradas despues de la limpieza:", df.shape[0])
