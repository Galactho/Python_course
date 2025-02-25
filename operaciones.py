'''
Este programa tiene las funciones para el buscador de texto
'''
from pathlib import Path
import re
import os
import datetime

patron = r'N\D{3}-\d{5}'
ruta = 'C:\\Users\\FERNANDOSANCHEZGONZA\\Desktop\\Mi_Gran_Directorio'        

def buscar(ruta,patron):
    '''
    Esta funcion recibe una ruta y un patro para buscarlo en los archivos
    Genera una cadena con el archivo y el patron encontrado en el
    '''
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        carpeta = Path(carpeta)
        for archivo in archivos:
            archivo_abierto = open(Path(carpeta/archivo),'r')
            resultado = re.search(patron, archivo_abierto.read())
            if resultado:
                archivo_abierto = Path(str(archivo_abierto))
                yield f'{archivo_abierto.stem}\t{resultado.group()}'

def tabla():
    '''
    Esta función es para darle formato a la tabla
    con los archivos y patrones encontrados en el
    '''
    print(f'''
ARCHIVO\t\tNRO. SERIE
-------\t\t----------''')
    g = buscar(ruta, patron)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
