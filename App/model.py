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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {'videos': None,
                'country': None,
                'video_category_id': None}

    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparecountries)
    catalog['video_category_id'] = lt.newList('ARRAY_LIST',
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

# Funciones de ordenamiento