import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
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

# Definimos el título deseado para la ventana de la figura
titulo_ventana = "Mapas de variables"

# Creamos la figura con el título especificado
plt.figure(titulo_ventana, figsize=(15, 7))

# Iteramos sobre cada columna y generamos un mapa para cada una
for i, col in enumerate(cols_to_check):
    # Calculamos la media de la columna
    mean_value = df[col].mean()

    # Creamos el mapa
    plt.subplot(2, 3, i + 1)
    m = Basemap(projection='merc', llcrnrlat=32, urcrnrlat=43,
                llcrnrlon=-125, urcrnrlon=-114, resolution='i')
    
    # Dibujamos costas, fronteras y límites de los países
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()

    # Convertimos coordenadas de longitud y latitud a coordenadas del mapa
    x, y = m(df['longitude'].values, df['latitude'].values)

    # Calculamos el rango de valores para la normalización del color
    vmin = df[col].min()
    vmax = df[col].max()

    # Normalizamos los valores para asignar colores
    norm = Normalize(vmin=vmin, vmax=vmax)

    # Aquí hay varias paletas de colores para elegir
    # plt.cm.inferno
    # plt.cm.plasma
    # plt.cm.magma
    # plt.cm.viridis
    # plt.cm.cividis
    # plt.cm.spring
    # plt.cm.summer
    cmap = plt.cm.viridis

    # Convertimos los valores a colores en la escala
    colors = cmap(norm(df[col]))

    # Pintamos los puntos en el mapa con los colores asignados
    plt.scatter(x, y, c=colors, marker='o', alpha=0.5)

    # Creamos una barra de color para la escala
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca(), orientation='horizontal')

    # Aádimos título al mapa, en este caso usaremos el nombre de la variable
    plt.title(f'{col}')
    
# Finalmente ajustamos la disposición de los subplots y mostramos la figura
plt.tight_layout()
plt.show()
