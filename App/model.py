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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time
import config as cf 
import datetime
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import mergesort as mes 
from DISClib.Algorithms.Sorting import quicksort as qus
from DISClib.DataStructures import arraylist as al


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {'videos': None,
                'video_category_id': None}

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST',
                                   cmpfunction=cmpVideosByViews)
    catalog['video_category_id'] = lt.newList(datastructure='ARRAY_LIST',
                                    cmpfunction=comparecategory_id)
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category_id):
    lt.addLast(catalog['video_category_id'], category_id)

# Funciones para creacion de datos
# Funciones de consulta
# Funciones utilizadas para comparar elementos dentro de una lista


def comparecategory_id(name, category_id):
    return (name == category_id['name'])

def cmpVideosByViews(video1, video2):
    if int(video1['views']) > int(video2['views']):
        return True
    elif int(video1['views']) < int(video2['views']):
        return False
    else: 
        if int(video1['likes']) > int(video2['likes']):
            return True
        else:
            return False

def cmpVideosbyId(video1,video2):
    rta= False
    if video1['video_id'] < video2['video_id']:
        rta= True
    return rta

def cmpVideosbyLikes(video1,video2):
    if video1['likes'] > video2['likes']:
        return True
    else:
        return False
# Funciones de ordenamiento
def sortVideos(lst,cmpfunction):
    sub_list = lst
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list= mes.sort(sub_list,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(round(elapsed_time_mseg, 2))
    return  sorted_list

#Funciones de requerimiento:
'Funciones de apoyo'
def category_id_name(catalog,category):
    for categoria in lt.iterator(catalog['video_category_id']):
        if category in categoria['name']:
            return categoria['id']

'Requerimiento #1'
def filtrar_PaisCategoria(catalog,country,category,size):
    videos = catalog['videos']
    sub_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(videos):
        if video['country']==country and video['category_id']==category:
                al.addLast(sub_list,video)  
    sorted_list= sortVideos(sub_list,cmpVideosByViews)  
    lst_n = lt.subList(sorted_list,1,size) 
    return filtrar_datos_req1(lst_n)

def filtrar_datos_req1(lst):
    lst_rta= lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(lst):
        video = {
            'trending_date': video['trending_date'],
            'title': video['title'],
            'publish_time': video['publish_time'],
            'views': int(video['views']),
            'likes': int(video['likes']),
            'dislikes': int(video["dislikes"]),                
        }
        lt.addLast(lst_rta,video)
    return lst_rta
'Requerimiento #2'

def filtar_paisTendencia(catalog, country):
    videos = catalog['videos']
    sub_list =  lt.newList(datastructure= 'ARRAY_LIST')
    for video in lt.iterator(videos):
        if video['country'] == country:
            lt.addLast(sub_list,video)
    srt_list = sortVideos(sub_list,cmpVideosbyId)
    lst = extraer_ids(srt_list)
    id,m = id_mas_repetido(lst)
    return (video_por_id(srt_list,id,m))

'Requerimiento #3'
def video_mas_dias_tendencia(catalog,id_category):
    videos = catalog['videos']
    sub_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(videos):
        if (video['category_id']== id_category) and (video['video_id']!= '#NAME?'):
            lt.addLast(sub_list,video)

    srt_list= sortVideos(sub_list,cmpVideosbyId)
    lst_ids = extraer_ids(srt_list)
    id_mayor, cant = id_mas_repetido(lst_ids)
    return video_por_id(sub_list,id_mayor,cant)

def extraer_ids(lst):
    sub_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(lst):
        lt.addLast(sub_list,video['video_id'])
    return sub_list


def id_mas_repetido(lst):
    id_mayor = 0
    id_cmp = 0
    for video_id in lt.iterator(lst):
        id_cant = lst['elements'].count(video_id)
        if id_cant > id_cmp:
            id_cmp = id_cant
            id_mayor = video_id
    return (id_mayor,id_cmp)

def video_por_id(lst,id_video,freq_id):
    for video in lt.iterator(lst):
        if video['video_id'] == id_video:
            info_video ={
                'title': video['title'],
                'cannel_title': video['cannel_title'],
                'category_id': video['category_id'],
                'dias': freq_id
            }
            return info_video

'Requerimiento #4'
def videos_mas_likes(catalog,country,cant_videos,tag):
    videos = catalog['videos']
    sub_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(videos):
        if (tag in video['tags']) and (video['country'] == country):
            lt.addLast(sub_list,video)
    srt_lst = sortVideos(sub_list,cmpVideosbyLikes)
    return lt.subList(srt_lst,1,cant_videos)

