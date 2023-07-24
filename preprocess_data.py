import sys
import os.path
import json
import cv2
import numpy
import shutil

def vector_de_intensidades(archivo_imagen):
    imagen_1 = cv2.imread(archivo_imagen, cv2.IMREAD_GRAYSCALE)
    imagen_2 = cv2.equalizeHist(imagen_1)
    imagen_2 = cv2.resize(imagen_2, (16, 16), interpolation=cv2.INTER_AREA)
    # flatten convierte una matriz de nxm en un array de largo nxm
    descriptor_imagen = imagen_2.flatten()
    return descriptor_imagen


def indexar(dir_dataset_r, dir_datos_temporales):
    if not os.path.isdir(dir_dataset_r):
        print("ERROR: no existe directorio {}".format(dir_dataset_r))
        sys.exit(1)
    elif os.path.exists(dir_datos_temporales):
        print("ERROR: ya existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
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
        lista_nombres.append(f'{dir_dataset_r}/{archivo}')
    numpy.save(f'{dir_datos_temporales}/descriptores.npy', matriz_desc)
    numpy.save(f'{dir_datos_temporales}/nombres.npy', lista_nombres)

dir_dataset_r = 'dataset'

# Create a directory with a subset of the dataset
os.makedirs('dataset_small', exist_ok=True)
for directory in os.listdir(dir_dataset_r):
    os.makedirs(f'dataset_small/{directory}', exist_ok=True)
    for i, file in enumerate(os.listdir(f'{dir_dataset_r}/{directory}')):
        if i % 1_000 == 0:
            shutil.copy(f'{dir_dataset_r}/{directory}/{file}', f'dataset_small/{directory}/{file}')

# Create a directory called descriptors_small and index the images in dataset_small
os.makedirs('descriptors_small', exist_ok=True)
for directory in os.listdir('dataset_small'):
    dir_datos_temporales = f'descriptors_small/{directory}'
    indexar(f'dataset_small/{directory}', dir_datos_temporales)