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

# Además, limpiamos los valores de longitud y latitud para que estén dentro de los rangos adecuados
df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]

# También limpiamos las filas que no contienen los valores específicos en la columna 'ocean_proximity'
valid_values = ['INLAND', '<1H OCEAN', 'NEAR BAY', 'NEAR OCEAN']
df = df[df['ocean_proximity'].isin(valid_values)]

# Finalmente mostramos de nuevo por pantalla el número de entradas tras la limpieza
print("Número de entradas despues de la limpieza:", df.shape[0])

# Ahora procedemos a calcular las medias de las siguiente variables:
# housing_median_age  
# total_rooms        
# total_bedrooms   
# population
# households      
# median_income 
# median_house_value
# Definimos la variable means y hacemos uso de la función mean para calcular la media de cada columna
# Por separado
# means = df[cols_to_check].mean(axis=0)

# Inicializamos una lista para guardar los valores de la media
means_list = []

# Calculamos la media de cada columna individualmente
for col in cols_to_check:
    # Sumamos todos los valores de la columna
    col_sum = df[col].sum()
    # Contamos el número de filas totales de dicha columna
    col_count = df[col].count()
    # Calculamos la media como la suma total entre el número de filas
    col_mean = col_sum / col_count
    # Agregamos el valor obtenido a la lista previamente definida
    means_list.append(col_mean)

# Tras esto tenemos una lista con las medias de las variables anteriormente mencionadas
# Ahora calcularemos las medianas de las mismas variables, para ello:
# Inicializamos una lista para guardar las medianas
medians_list = []

# Calculamos la mediana de cada columna individualmente
for col in cols_to_check:
    # Ordenamos los valores de la columna
    sorted_values = df[col].sort_values()
    # Contamos el número total de entradas de la variable
    col_count = sorted_values.count()
    # Calculamos el índice medio
    middle_index = col_count // 2
    # Si el número de valores es impar, la mediana es el valor en el índice medio
    if col_count % 2 != 0:
        col_median = sorted_values.iloc[middle_index]
    # Si el número de valores es par, la mediana es el promedio de los dos valores en el medio
    else:
        col_median = (sorted_values.iloc[middle_index - 1] + sorted_values.iloc[middle_index]) / 2
    # Agregamos la mediana calculada a la lista de medianas
    medians_list.append(col_median)

# Ahora calcularemos los valores mínimos y máximos de cada variable, para ello:
# Inicializamos las  listas para almacenar los mínimos y máximos de cada columna
min_values = []
max_values = []

# Calculamos los mínimos y máximos de cada columna individualmente
for col in cols_to_check:
    # Calculamos el mínimo valor de la columna y lo agregamos  a la lista de mínimos usando la función min()
    min_val = df[col].min()
    min_values.append(min_val)
    
    # Calculamos el máximo valor de la columna y lo agregamos a la lista de máximos usando la función max()
    max_val = df[col].max()
    max_values.append(max_val)

# Ahora calcularemos la desviación típica de cada variable, para ello:
# Podemos hacer uso de la fórmula matemática para calcular la desviación típica, o podemos hacer uso de una 
# Función de la librería Pandas para calcularla de forma más sencilla
# Vamos a optar por esta segunda opción para que podais apreciar algunas ventajas que nos proporciona
# el uso de librerías externas
# Inicializamos una lista para almacenar las desviaciones estándar de cada columna
std_devs = []

# Calculamos las desviaciones estándar de cada columna individualmente
for col in cols_to_check:
    # Calculamos la desviacón estándar usando la función std() y la agregamos a la lista
    std_dev = df[col].std()
    std_devs.append(std_dev)

# Inicializar una lista para almacenar las varianzas de cada columna
variances = []

# Calcular las varianzas de cada columna individualmente
for col in cols_to_check:
    # Calcular la media de la columna
    col_mean = df[col].mean()
    # Calcular las desviaciones de cada valor respecto a la media
    deviations = df[col] - col_mean
    # Elevar al cuadrado cada desviación
    squared_deviations = deviations ** 2
    # Calcular la varianza como la media de los cuadrados de las desviaciones
    variance = squared_deviations.mean()
    # Agregar la varianza calculada a la lista
    variances.append(variance)

# Inicializamos una lista para almacenar las varianzas de cada columna
variances2 = []

# Calcular las varianzas de cada columna individualmente
# Usamos la función zip() para combinar las listas cols_to_check y std_dev
# De este modo en cada iteración del bucle for, col tomará un valor de cols_to_check
# Y std_dev tomará el valor de cada deviacón estándar de la lista std_devs
for col, std_dev in zip(cols_to_check, std_devs):
    # Elevamos al cuadrado la desviación estándar
    squared_deviation = std_dev ** 2
    # Agregamos la varianza calculada a la lista
    variances.append(squared_deviation)


