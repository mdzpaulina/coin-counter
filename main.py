import cv2
import numpy as np
import desenfoque_gaussiano as dg


# Cargar imagen
imagen_original = cv2.imread("monedas_5.jpg")

# Achicar la imagen a la mitad de su tamaño
imagen_original = imagen_original[::2, ::2]

# Convertir a escala de grises y aplicar filtro gaussiano
gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
blur = dg.filtro_gaussiano(gris, 6)

# Detectar círculos
circulos = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=100,
    param2=30,
    minRadius=30,
    maxRadius=80
)
# Dibujar círculos detectados
imagen = imagen_original.copy()
if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")
    for (x, y, r) in circulos:
        cv2.circle(imagen, (x, y), r, (0, 255, 0), 2)
        cv2.putText(imagen, f"{r}px", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


# Mostrar imagen
cv2.imshow("Círculos detectados", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
