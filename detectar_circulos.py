import cv2
import numpy as np

#Detección de círculos de diferente tamaño (monedas)
def detectar_circulos(imagen):
    # Detectar círculos utilizando la transformada de Hough
    circulos = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                param1=50, param2=30, minRadius=5, maxRadius=100)

    # Si se detectan círculos, dibujarlos en la imagen original
    if circulos is not None:
        circulos = np.uint16(np.around(circulos))
        for i in circulos[0, :]:
            # Dibujar el círculo exterior
            cv2.circle(imagen, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Dibujar el centro del círculo
            cv2.circle(imagen, (i[0], i[1]), 2, (0, 0, 255), 3)
    return imagen

