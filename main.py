import cv2
import numpy as np
import funciones.preprocesamiento as pp
import funciones.clasificacion as cl

# Cargar imagen
imagen_original = cv2.imread("./IMGs_monedas/monedas_7.jpg")

#Procesar imagen
imagen_original, imagen_blur = pp.procezamiento(imagen_original)

# Detectar círculos
circulos = cv2.HoughCircles(
    imagen_blur,
    cv2.HOUGH_GRADIENT,
    dp = 1.2,
    minDist = 50,
    param1 = 100,
    param2 = 30,
    minRadius = 40,
    maxRadius = 80
)

# Copiar imagen para dibujar resultados
imagen = imagen_original.copy()

# Dibujar y clasificar círculos
conteo, valor_total = cl.clasificacion(imagen, circulos)

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
