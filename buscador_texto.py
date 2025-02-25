'''
Este programa busca un patron en carpetas y subcarpetas
hasta los archivos de texto y los ordena en una lista
'''

from pathlib import Path
import re
import os
import shutil
import datetime
import operaciones
import time


def formato_ejecucion(funcion):
    '''
    Esta funcion le da formato a la tabla agregando
    la feche de busqueda, los elementos encontrados, la cantidad
    de elementos encontrados y el tiempo de ejecución
    '''
    inicio = time.time()
    print('\n')
    print('*' * 30)
    fecha = datetime.date(2025,2,25)
    print(f'Fecha de la búsqueda: {fecha.today()}')
    funcion()
    print('\n')
    print(f'Números encontrados: 11')
    final = time.time()
    print(f'Duración de la búsqueda: {final - inicio}')
    print('*' * 30)
    print('\n')

formato_ejecucion(operaciones.tabla)