import cv2
import numpy as np
import desenfoque_gaussiano as dg

# Cargar imagen
imagen_original = cv2.imread("./IMGs_monedas/monedas_7.jpg")

# Achicar la imagen a la mitad de su tamaño
imagen_original = imagen_original[::2, ::2]

# Convertir a escala de grises y aplicar desenfoque
gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
blur = dg.filtro_gaussiano(gris, 5)


# Detectar círculos
circulos = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp = 1.2,
    minDist = 50,
    param1 = 100,
    param2 = 30,
    minRadius = 40,
    maxRadius = 80
)

valor_total = 0
conteo = {1: 0, 2: 0, 5: 0, 10: 0}

# Copiar imagen para dibujar resultados
imagen = imagen_original.copy()

# Dibujar y clasificar círculos
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

# Mostrar resumen en la imagen
texto = f"Total: ${valor_total} | $1:{conteo[1]} $2:{conteo[2]} $5:{conteo[5]} $10:{conteo[10]}"
cv2.rectangle(imagen, (0, 0), (imagen.shape[1], 25), (255, 255, 255), -1)
cv2.putText(imagen, texto, (10, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

# Mostrar imagen
cv2.imshow("Detección de Monedas", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar resumen en consola
print("\nResumen de monedas detectadas:")
for val in [1, 2, 5, 10]:
    print(f"Monedas de ${val}: {conteo[val]}")
print(f"Valor total: ${valor_total}")
