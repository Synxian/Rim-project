import cv2

def vector_de_intensidades(archivo_imagen):
    imagen_1 = cv2.imread(archivo_imagen, cv2.IMREAD_GRAYSCALE)
    imagen_2 = cv2.equalizeHist(imagen_1)
    imagen_2 = cv2.resize(imagen_2, (22, 22), interpolation=cv2.INTER_AREA)
    # flatten convierte una matriz de nxm en un array de largo nxm
    descriptor_imagen = imagen_2.flatten()
    return descriptor_imagen
