import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Cargar el archivo CSV
df = pd.read_csv('housing.csv')

print("Número de entradas antes de la limpieza:", df.shape[0])

# Creamos una lista que contiene los nombres de las columnas que queremos verificar
cols_to_check = ['total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

# Iteramos por todas las columnas y nos quedamos sólo con aquellas cuyos valores sean mayores que cero
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

# Calcular la matriz de correlación
correlation_matrix = df[cols_to_check].corr()

# Cargamos el archivo de shapefile para dibujar los límites geográficos de California, lo he sacado de la página oficial del 
# Gobierno de California
california = gpd.read_file("./tl_2019_06_cousub")

# Definimos el título deseado para la ventana de la figura
titulo_ventana = "Mapas de correlaciones"

# Creamos la figura con el título especificado
plt.figure(titulo_ventana, figsize=(25, 12))

# Iteramos sobre cada columna y generamos un mapa para cada una
for i, col in enumerate(cols_to_check):
    # Calculamos la media de la columna
    mean_value = df[col].mean()

    # Creamos el subplot y lo proyectamos sobre el mapa de California
    ax = plt.subplot(2, 3, i + 1)
    california.plot(ax=ax, color='lightgreen')
    
    # Convertimos coordenadas de longitud y latitud a coordenadas del mapa
    x, y = df['longitude'].values, df['latitude'].values

    # Calculamos el rango de valores para la normalización del color
    vmin = -1.0
    vmax = 1.0

    # Normalizamos los valores para asignar colores
    norm = Normalize(vmin=vmin, vmax=vmax)

    # Escogemos una paleta de colores centrada en 0
    cmap = plt.cm.seismic

    # Convertimos los valores de correlación a colores en la escala
    colors = cmap(norm(correlation_matrix[col]))

    # Pintamos los puntos en el mapa con los colores asignados
    ax.scatter(x, y, c=colors, marker='.', alpha=0.1)

    # Creamos una barra de color para la escala
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='horizontal')

    # Añadimos título al mapa, en este caso usaremos el nombre de la variable
    ax.set_title(f'Correlación con {col}')

# Finalmente ajustamos la disposición de los subplots y mostramos la figura
plt.tight_layout()
plt.show()

