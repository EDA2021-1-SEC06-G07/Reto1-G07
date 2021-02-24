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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(lst_tipo):

    catalog = {'videos': None,
                'country': None,
                'video_category_id': None}

    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList(datastructure=lst_tipo,
                                    cmpfunction=comparecountries)
    catalog['video_category_id'] = lt.newList(datastructure=lst_tipo,
                                    cmpfunction=comparecategory_id)
    

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    countries = video['country'].split(",")
    for country in countries:
        addVideoCountry(catalog, country.strip(), video)


def addVideoCountry(catalog, countryname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    countries = catalog['country']
    poscountry = lt.isPresent(countries, countryname)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)


def addCategory(catalog, category_id):
    """
    Adiciona un tag a la lista de tags
    """
    t = newCategory(category_id['name'],category_id['id'])
    lt.addLast(catalog['video_category_id'], t)

# Funciones para creacion de datos
def newCountry(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    country = {'name': "", "videos": None, "average_rating": 0}
    country['name'] = name
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def newCategory(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category_id = {'name':'' ,'id':'' }
    category_id['name'] = name
    category_id['id'] = id
    return category_id

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecountries(comparecountries1, country):
    if (comparecountries1.lower() in country['name'].lower()):
        return 0
    return -1

def comparecategory_id(name, category_id):
    return (name == category_id['name'])

def cmpVideosByViews(video1, video2):
    if int(video1['views']) < int(video2['views']):
        return True
    elif int(video1['views']) > int(video2['views']):
        return False
    else: 
        if int(video1['likes']) < int(video2['likes']):
            return True
        else:
            return False

# Funciones de ordenamiento
def sortVideos(catalog, size, sort_tipo):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list= 'No se pudo ordenar la lista'
    if sort_tipo == 'selection':
        sorted_list= ses.sort(sub_list, cmpVideosByViews)
    elif sort_tipo == 'insertion':
        sorted_list= ins.sort(sub_list, cmpVideosByViews)
    elif sort_tipo == 'shell':
        sorted_list= shs.sort(sub_list, cmpVideosByViews) 
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return round(elapsed_time_mseg, 2), sorted_list
