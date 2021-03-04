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
    print("1- Cargar información en el catálogo")
    print("2- Ordenar la información del cátalogo!")
    print("3- Encontrar el video tendencia por país")
    print("4- Encontrar el video tendencia por categoría")
    print("5- Buscar los videos con más likes de un país")
    print("0- Salir")
    
def initCatalog(lst_tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(lst_tipo)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        ident = str(input('Digite el tipo de representación de lista \n ARRAY_LIST(AL) o LINKED_LIST(LL): '))
        if (ident == 'AL') or (ident =='LL'): 
            lst_tipo = None
            if ident == 'AL':
                lst_tipo= 'ARRAY_LIST'
            else:
                lst_tipo= 'LINKED_LIST'

            print("Cargando información de los archivos ....")
            catalog = initCatalog(lst_tipo)
            t1= t.process_time()
            loadData(catalog)
            t2= t.process_time()
            print("Tiempo: {:} s".format(t2-t1))
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        else:
            print('*El tipo de lista no es correto*')
            
        
    elif int(inputs[0]) == 2:
        cant_datos= int(input('Digite el tamaño de la muestra a cargar: '))
        sort_tipo= str(input('Digite el tipo de ordenamiento que quiere realizar \n(selection, insertion, shell, merge o quick): '))
        print ("Organizando Datos...")
        result= controller.sortVideos(catalog, cant_datos, sort_tipo)
        time, sorted_list= result
        print('Videos cargados: '+ str(lt.size(sorted_list)))
        print('tiempo de carga: '+ str(time)+' ms')

    elif int(inputs[0]) == 3:
        pass52
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
