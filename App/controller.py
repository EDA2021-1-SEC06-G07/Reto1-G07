"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from datetime import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(lst_tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(lst_tipo)
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    file = cf.data_dir + 'videos-large.csv'
    
    input_file = csv.DictReader(open(file, encoding= 'utf-8'))
    for i in input_file:
        sub_catalog = {
            'video_id': i['video_id'],
            'trending_date': datetime.strptime(i['trending_date'], '%y.%d.%m').date(),
            'category_id': int(i['category_id']),
            'views': int(i['views']),
            'likes': int(i['likes'])                      
        }
        model.addVideo(catalog,sub_catalog)
    

# Funciones de ordenamiento
def sortVideos(catalog, size, sort_tipo):
    return model.sortVideos(catalog, size, sort_tipo)

# Funciones de consulta sobre el catálogo
