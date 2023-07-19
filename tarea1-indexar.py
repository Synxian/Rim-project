# CC5213 - TAREA 1
# 27 de marzo de 2023
# Alumno: Felix Melo

import sys
import os.path
import json
import cv2
import numpy

def vector_de_intensidades(archivo_imagen):
    imagen_1 = cv2.imread(archivo_imagen, cv2.IMREAD_GRAYSCALE)
    imagen_2 = cv2.equalizeHist(imagen_1)
    imagen_2 = cv2.resize(imagen_2, (22, 22), interpolation=cv2.INTER_AREA)
    # flatten convierte una matriz de nxm en un array de largo nxm
    descriptor_imagen = imagen_2.flatten()
    return descriptor_imagen


def tarea1_indexar(dir_dataset_r, dir_datos_temporales):
    if not os.path.isdir(dir_dataset_r):
        print("ERROR: no existe directorio {}".format(dir_dataset_r))
        sys.exit(1)
    elif os.path.exists(dir_datos_temporales):
        print("ERROR: ya existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
    # borrar la siguiente linea
    # Implementar la tarea:
    #  1-leer imágenes en dir_dataset_r
    #  2-calcular descriptores de imágenes
    #  3-crear dir_datos_temporales con: os.makedirs(dir_datos_temporales, exist_ok=True)
    #  4-escribir en dir_datos_temporales los descriptores
    matriz_desc=[]
    lista_nombres=[]
    os.makedirs(dir_datos_temporales, exist_ok=True)
    for archivo in os.listdir(dir_dataset_r):
        descriptor = vector_de_intensidades(f'{dir_dataset_r}/{archivo}')
        if len(matriz_desc) == 0:
            matriz_desc = descriptor
        else:
            matriz_desc = numpy.vstack([matriz_desc, descriptor])
        # agregar nombre del archivo a la lista de nombres
        lista_nombres.append(archivo)
    numpy.savetxt(f'{dir_datos_temporales}/descriptores.txt', matriz_desc, fmt='%d')
    numpy.savetxt(f'{dir_datos_temporales}/nombres.txt', lista_nombres, fmt='%s')
# inicio de la tarea
if len(sys.argv) < 3:
    print("Uso: {} [dir_dataset_r] [dir_datos_temporales]".format(sys.argv[0]))
    sys.exit(1)

dir_dataset_r = sys.argv[1]
dir_datos_temporales = sys.argv[2]

# llamar a la funcion
tarea1_indexar(dir_dataset_r, dir_datos_temporales)
