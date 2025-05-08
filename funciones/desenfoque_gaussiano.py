import cv2
import numpy as np

def filtro_gaussiano(imagen, tamaño):
    """
    Aplica un filtro gaussiano 2D manual para suavizar la imagen.

    Parámetros:
        imagen (np.array): Imagen original.
        tamaño (int): Tamaño del kernel.

    Retorna:
        np.array: Imagen filtrada.
    """
    sig = (tamaño-1)/3
    # Generar vector gaussiano 1D
    d = np.arange(-(tamaño-1)/2, (tamaño-1)/2+1).astype(int)           
    s = np.exp(-(np.power(d,2))/(2*np.power(sig,2)))
    # Crear kernel gaussiano 2D como producto exterior
    kernel = np.zeros((tamaño, tamaño))
    for yi in range(tamaño):             
        for xi in range(tamaño):
            kernel[yi, xi]=s[yi]*s[xi]
    kernel /= kernel.sum()
    # Aplicar convolución con el kernel
    imagen_filtrada = cv2.filter2D(imagen, -1, kernel)
    return imagen_filtrada