import sys
import os.path
from common import angulos_por_zona
import cv2
import numpy
import shutil

def indexar(directory, dir_datos_temporales):
    if not os.path.isdir(directory):
        print("ERROR: no existe directorio {}".format(directory))
        sys.exit(1)
    elif os.path.exists(dir_datos_temporales):
        print("ERROR: ya existe directorio {}".format(dir_datos_temporales))
        sys.exit(1)
    matriz_desc=[]
    lista_nombres=[]
    os.makedirs(dir_datos_temporales, exist_ok=True)
    for archivo in os.listdir(directory):
        descriptor = angulos_por_zona(f'{directory}/{archivo}')
        if len(matriz_desc) == 0:
            matriz_desc = descriptor
        else:
            matriz_desc = numpy.vstack([matriz_desc, descriptor])
        # agregar nombre del archivo a la lista de nombres
        lista_nombres.append(f'{directory.split("/")[1]}/{archivo}')
    numpy.save(f'{dir_datos_temporales}/descriptores.npy', matriz_desc)
    numpy.save(f'{dir_datos_temporales}/nombres.npy', lista_nombres)

dir_dataset_r = 'dataset'

# # Create a directory with a subset of the dataset
# os.makedirs('dataset_small', exist_ok=True)
# for directory in os.listdir(dir_dataset_r):
#     os.makedirs(f'dataset_small/{directory}', exist_ok=True)
#     cantidad = len(os.listdir(f'{dir_dataset_r}/{directory}')) // 50
#     for i, file in enumerate(os.listdir(f'{dir_dataset_r}/{directory}')):
#         if i % cantidad == 0:
#             shutil.copy(f'{dir_dataset_r}/{directory}/{file}', f'dataset_small/{directory}/{file}')

# Create a directory called descriptors_small and index the images in dataset_small
os.makedirs('descriptors_small', exist_ok=True)
for directory in os.listdir('dataset_small'):
    dir_datos_temporales = f'descriptors_small/{directory}'
    indexar(f'dataset_small/{directory}', dir_datos_temporales)



# os.makedirs('micro_dataset', exist_ok=True)
# for directory in os.listdir(dir_dataset_r):
#     os.makedirs(f'micro_dataset/{directory}', exist_ok=True)
#     cantidad = len(os.listdir(f'{dir_dataset_r}/{directory}')) // 10
#     for i, file in enumerate(os.listdir(f'{dir_dataset_r}/{directory}')):
#         if i % cantidad == 0:
#             shutil.copy(f'{dir_dataset_r}/{directory}/{file}', f'micro_dataset/{directory}/{file}')


os.makedirs('descriptors_micro', exist_ok=True)
for directory in os.listdir('micro_dataset'):
    dir_datos_temporales = f'descriptors_micro/{directory}'
    indexar(f'micro_dataset/{directory}', dir_datos_temporales)
