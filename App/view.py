"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as al
assert cf
import time as t

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de los archivos de video.")
    print("2- Req_1: Encontrar buenos videos por categoria y país.")
    print("3- Encontrar el video tendencia por país")
    print("4- Req_2: Encontrar el video con más días de tendencia por categoría")
    print("5- Buscar los videos con más likes de un país")
    print("0- Salir")
    
def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadVideos(catalog)
    controller.loadCategory_id(catalog)

catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
            print("Cargando información de los archivos ...")
            catalog = initCatalog()
            t1= t.process_time()
            loadData(catalog)
            t2= t.process_time()
            print("Tiempo: {:} s".format(t2-t1))
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            fv = al.firstElement(catalog['videos'])
            print('Primer video: ' +str(fv['title'])+', '+str(fv['cannel_title'])+', '+str(fv['trending_date'])+', '
                    +str(fv['country'])+', views: '+str(fv['views'])+', likes: ' +str(fv['likes'])+', dislikes: '+str(fv['dislikes']))
            print(catalog['video_category_id'])
       
            
        
    elif int(inputs[0]) == 2:
            cant_vd = int(input('Ingrese el tamaño del ranking: '))
            country = str(input('Ingrese el país de los videos a analizar: '))
            category = str(input('Ingresa la categoria de los videos a analizar: '))
            id_category= int(controller.category_id_name(catalog,category))
            print(controller.load_Req_1(catalog,country,id_category,cant_vd))


    elif int(inputs[0]) == 3:
        country = str(input("Ingrese el país:"))
        list_id = controller.load_req2(catalog,country) 
        print (list_id)
        
    elif int(inputs[0]) == 4:
        category = str(input('Ingrese la categoria a analizar: '))
        id_category = int(controller.category_id_name(catalog,category))
        print(controller.load_Req_3(catalog,id_category))
        
    elif int(inputs[0]) == 5:
        country = str(input('Ingrese país: '))
        v_cant = int(input('Ingrese cant: '))
        tag = str(input('Ingrese tag: '))
        lst = controller.load_Req_4(catalog,country,v_cant,tag)
        for fv in lt.iterator(lst):
            print('video: ' +str(fv['title'])+', '+str(fv['cannel_title'])+', '+str(fv['publish_time'])+
                    ', views: '+str(fv['views'])+', likes: ' +str(fv['likes'])+', dislikes: '+str(fv['dislikes'])+
                    ', tags: '+str(fv['tags']))
    else:
        sys.exit(0)
sys.exit(0)
