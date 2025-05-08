import cv2
import funciones.desenfoque_gaussiano as dg


def procesamiento(imagen):
    """
    Realiza el preprocesamiento de la imagen para facilitar la detección de círculos.

    Pasos:
    - Redimensiona la imagen a la mitad.
    - Convierte la imagen a escala de grises.
    - Aplica un filtro gaussiano para reducir el ruido.

    Parámetros:
        imagen (np.array): Imagen original cargada con OpenCV.

    Retorna:
        tuple: Imagen redimensionada y su versión desenfocada en escala de grises.
    """
    # Redimensionar la imagen a la mitad para reducir el tamaño de procesamiento
    imagen_original = imagen[::2, ::2]

    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque gaussiano personalizado para suavizar la imagen
    blur = dg.filtro_gaussiano(gris, 5)

    # Retornar la imagen procesada (original reducida y desenfocada)
    return imagen_original, blur
