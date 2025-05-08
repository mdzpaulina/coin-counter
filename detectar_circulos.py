import cv2
import numpy as np
import desenfoque_gaussiano as dg

# Cargar imagen
imagen_original = cv2.imread("./IMGs_monedas/monedas_1.jpg")

#achicar la imagen el doble de su tamaño
imagen_original = cv2.resize(imagen_original, (0, 0), fx=0.5, fy=0.5)

gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
blur = dg.filtro_gaussiano(gris, 5)

# Ventana con trackbars
cv2.namedWindow("Ajuste de Círculos")

def nothing(x):
    pass

# Crear trackbars
cv2.createTrackbar("minRadius", "Ajuste de Círculos", 32, 100, nothing)
cv2.createTrackbar("maxRadius", "Ajuste de Círculos", 80, 150, nothing)
cv2.createTrackbar("param2", "Ajuste de Círculos", 30, 100, nothing)

while True:
    # Leer valores de los trackbars
    min_radius = cv2.getTrackbarPos("minRadius", "Ajuste de Círculos")
    max_radius = cv2.getTrackbarPos("maxRadius", "Ajuste de Círculos")
    param2 = cv2.getTrackbarPos("param2", "Ajuste de Círculos")
    
    cv2.waitKey(100)

    # Copiar imagen original
    imagen = imagen_original.copy()

    # Detectar círculos con los valores actuales
    circulos = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=param2,
        minRadius=min_radius,
        maxRadius=max_radius,
    )

    valor_total = 0
    conteo = {1: 0, 2: 0, 5: 0, 10: 0}
    
    # Dibujar círculos detectados
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
            elif 60 <= r <= 65:
                valor = 10
            else:
                valor = 0  # fuera de rango
            
            if valor > 0:
                conteo[valor] += 1
                valor_total += valor
                
    # Mostrar conteo y total en la imagen
    texto = f"Total: ${valor_total} | $1:{conteo[1]} $2:{conteo[2]} $5:{conteo[5]} $10:{conteo[10]}"
    cv2.rectangle(imagen, (0, 0), (imagen.shape[1], 25), (255, 255, 255), -1)
    cv2.putText(imagen, texto, (10, 18),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # Mostrar imagen
    cv2.imshow("Ajuste de Círculos", imagen)

    # Salir con tecla ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

# Mostrar resumen final en consola
print("\nResumen de monedas detectadas:")
for val in [1, 2, 5, 10]:
    print(f"Monedas de ${val}: {conteo[val]}")
print(f"Valor total: ${valor_total}")