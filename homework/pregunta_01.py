"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
import pandas as pd

def pregunta_01():

    with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()


    data = []
    cluster = None
    for line in lines[4:]:
        if line.strip():
            parte = line.split()
            if parte[0].isdigit():
                if cluster:
                    data.append(cluster)
                cluster = int(parte[0])
                cantidad_de_palabras_clave = int(parte[1])
                porcentaje_de_palabras_clave = float(parte[2].replace(',', '.').replace('%', ''))
                principales_palabras_clave = ' '.join(parte[3:])
                cluster = {
                    'cluster': cluster,
                    'cantidad_de_palabras_clave': cantidad_de_palabras_clave,
                    'porcentaje_de_palabras_clave': porcentaje_de_palabras_clave,
                    'principales_palabras_clave': principales_palabras_clave
                }
            else:
                cluster['principales_palabras_clave'] += ' ' + ' '.join(parte)

    if cluster:
        data.append(cluster)
    df = pd.DataFrame(data)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(' ,', ',').str.replace(', ', ', ').str.replace('  ', ' ').str.strip('.').str.lstrip('% ')
    return df

print(pregunta_01())
