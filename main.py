import os
import cv2
from desenfoque_gaussiano import filtro_gaussiano
import pytesseract
# Ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ruta actual del script
carpeta_actual = os.path.dirname(__file__)

# Carga de la imagen
imagen_monedas = cv2.imread(os.path.join(carpeta_actual, "monedas.jpeg"))
imagen_monedas2 = cv2.imread(os.path.join(carpeta_actual, "monedas2.jpg"))

# Desenfoque Gaussiano
monedas_suavizado = filtro_gaussiano(imagen_monedas, 5)
monedas_suavizado2 = filtro_gaussiano(imagen_monedas2, 20)

# Escala de grises
monedas_gris = cv2.cvtColor(monedas_suavizado, cv2.COLOR_BGR2GRAY)
monedas_gris2 =  cv2.cvtColor(monedas_suavizado2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gris", monedas_gris)

# Deteccion de círculos



cv2.waitKey(0)
cv2.destroyAllWindows()