# CC5213 - TAREA 1
# 27 de marzo de 2023
# Alumno: [nombre]

import sys
import os.path
import cv2
import scipy.spatial
import numpy


def tarea1_buscar(dir_dataset_q, dir_datos_temporales, file_resultados):
    if not os.path.isdir(dir_dataset_q):
        print("ERROR: no existe directorio {}".format(dir_dataset_q))
        sys.exit(1)
    elif not os.path.isdir(dir_datos_temporales):
        print("ERROR: no existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
    elif os.path.exists(file_resultados):
        print("ERROR: ya existe archivo {}".format(file_resultados))
        sys.exit(1)
    # borrar la siguiente linea
    # Implementar la busqueda
    #  1-leer imágenes en dir_dataset_q y calcular descriptores
    #  2-leer descriptores de R de dir_datos_temporales
    #  3-para cada descriptor q localizar el mas cercano en R
    #  4-escribir en file_resultados
    matriz_r = numpy.loadtxt(f'{dir_datos_temporales}/descriptores.txt')
    nombres_r = numpy.loadtxt(f'{dir_datos_temporales}/nombres.txt', dtype=str)
    matriz_desc=[]
    lista_nombres=[]
    resultados=[]
    for archivo in os.listdir(dir_dataset_q):
        descriptor = vector_de_intensidades(f'{dir_dataset_q}/{archivo}')
        if len(matriz_desc) == 0:
            matriz_desc = descriptor
        else:
            matriz_desc = numpy.vstack([matriz_desc, descriptor])
        # agregar nombre del archivo a la lista de nombres
        lista_nombres.append(archivo)
    matriz_distancias = scipy.spatial.distance.cdist(matriz_desc, matriz_r, metric='cityblock')
    for i in range(len(lista_nombres)):
        min_ind = numpy.argmin(matriz_distancias[i])
        name = nombres_r[min_ind]
        resultados.append([lista_nombres[i], name, matriz_distancias[i][min_ind]])
    with open(file_resultados, 'w') as f:
        for i in resultados[:-1]:
            f.write(f'{i[0]}\t{i[1]}\t{i[2]}\n')
        f.write(f'{resultados[-1][0]}\t{resultados[-1][1]}\t{resultados[-1][2]}')


# inicio de la tarea
if len(sys.argv) < 4:
    print("Uso: {} [dir_dataset_q] [dir_datos_temporales] [resultados.txt]".format(sys.argv[0]))
    sys.exit(1)

dir_dataset_q = sys.argv[1]
dir_datos_temporales = sys.argv[2]
file_resultados = sys.argv[3]
data={}
tarea1_buscar(dir_dataset_q, dir_datos_temporales, file_resultados)
