import cv2
import funciones.desenfoque_gaussiano as dg

def procezamiento(imagen):
    """
    Esta función se encarga de realizar el preprocesamiento de los datos.
    """
    # Achicar la imagen a la mitad de su tamaño
    imagen_original = imagen[::2, ::2]

    # Convertir a escala de grises y aplicar desenfoque
    gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
    blur = dg.filtro_gaussiano(gris, 5)

    return imagen_original, blur