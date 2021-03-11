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
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadVideos(catalog):
    file = cf.data_dir + 'videos-large.csv'
    
    input_file = csv.DictReader(open(file, encoding='utf-8',errors='ignore'))
    for video in input_file:
        sub_catalog = {
            'video_id': video['video_id'],
            'trending_date': str(video['trending_date']),
            'title': video['title'],
            'cannel_title': video['channel_title'],
            'category_id': int(video['category_id']),
            'publish_time': video['publish_time'],
            'tags': str(video['tags']),
            'views': int(video['views']),
            'likes': int(video['likes']),
            'dislikes': int(video["dislikes"]), 
            'country': video['country']                 
        }
        model.addVideo(catalog,sub_catalog)
    
def loadCategory_id(catalog):
    file = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8',errors='ignore'),delimiter='\t')
    for category in input_file:
        sub_catalog = {
            'id': category['id'],
            'name': category['name']
        }
        model.addCategory(catalog, sub_catalog)

# Funciones de ordenamiento
# Funciones de consulta sobre el catálogo
# Funciones de requerimiento:
def load_Req_1(catalog, country, category,size):
    return  model.filtrar_PaisCategoria(catalog,country, category,size)
def load_req2(catalog, country):
    return model.filtar_paisTendencia(catalog, country)
def load_Req_3(catalog,category):
    return model.video_mas_dias_tendencia(catalog,category)
def category_id_name(catalog,category):
    return model.category_id_name(catalog,category)
def load_Req_4(catalog,country,cant_videos,tag):
    return model.videos_mas_likes(catalog,country,cant_videos,tag)
