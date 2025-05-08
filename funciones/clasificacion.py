import cv2
import numpy as np

def clasificacion(imagen, circulos):
    ''' 
    Esta función se encarga de clasificar los círculos detectados en la imagen.
    Se espera que la imagen ya haya sido preprocesada y que los círculos hayan sido detectados.
    '''
    valor_total = 0
    conteo = {1: 0, 2: 0, 5: 0, 10: 0}

    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype("int")
        for (x, y, r) in circulos:
            cv2.circle(imagen, (x, y), r, (0, 255, 0), 2)
            cv2.putText(imagen, f"{r}px", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            if 43 <= r <= 50:
                valor = 1
            elif 51 <= r <= 55:
                valor = 2
            elif 56 <= r <= 59:
                valor = 5
            elif 60 <= r <= 66:
                valor = 10
            else:
                valor = 0

            if valor > 0:
                conteo[valor] += 1
                valor_total += valor
    return conteo, valor_total

