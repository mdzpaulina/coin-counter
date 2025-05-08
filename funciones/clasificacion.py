import cv2
import numpy as np


def clasificacion(imagen, circulos):
    """
    Clasifica los círculos detectados en la imagen según su radio.

    Parámetros:
        imagen (np.array): Imagen original donde se dibujarán los círculos.
        circulos (np.array): Arreglo de círculos detectados por HoughCircles.

    Retorna:
        tuple: (conteo de monedas por valor, valor total)
    """
    # Inicializar el valor total y el diccionario para contar monedas por valor
    valor_total = 0
    conteo = {1: 0, 2: 0, 5: 0, 10: 0}

    # Verificar que se hayan detectado círculos
    if circulos is not None:
        # Redondear los valores y convertirlos a enteros
        circulos = np.round(circulos[0, :]).astype("int")

        # Recorrer cada círculo detectado
        for (x, y, r) in circulos:
            # Dibujar el contorno del círculo en verde
            cv2.circle(imagen, (x, y), r, (0, 255, 0), 2)

            # Mostrar el radio en píxeles sobre la imagen
            cv2.putText(
                imagen, f"{r}px", (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1
            )

            # Clasificar el valor de la moneda según el radio
            if 43 <= r <= 50:
                valor = 1
            elif 51 <= r <= 55:
                valor = 2
            elif 56 <= r <= 59:
                valor = 5
            elif 60 <= r <= 66:
                valor = 10
            else:
                valor = 0  # Valor desconocido o fuera de rango

            # Sumar al conteo y al valor total si se reconoció un valor válido
            if valor > 0:
                conteo[valor] += 1
                valor_total += valor

    # Retornar el conteo de monedas y la suma total
    return conteo, valor_total
