# 💰 Detección y Clasificación de Monedas Mexicanas con OpenCV

Este proyecto utiliza **Python**, **OpenCV** y **NumPy** para detectar monedas mexicanas en imágenes y clasificar su valor (1, 2, 5 y 10 pesos) automáticamente a partir del tamaño de cada moneda.

## 🗂️ Estructura del Proyecto

```
.
├── main.py
├── README.md
├── funciones/
│   ├── clasificacion.py
│   ├── desenfoque_gaussiano.py
│   └── preprocesamiento.py
└── IMGs_monedas/
    ├── monedas_1.jpg
    ├── monedas_2.jpg
    ├── monedas_3.jpg
    ├── monedas_4.jpg
    ├── monedas_5.jpg
    ├── monedas_6.jpg
    └── monedas_7.jpg
```

## 🧠 ¿Qué hace el programa?

1. **Carga una imagen** desde la carpeta `IMGs_monedas`.
2. **Reduce su tamaño** para facilitar el procesamiento.
3. **Convierte a escala de grises y aplica un desenfoque gaussiano.**
4. **Detecta círculos** con la transformada de Hough para identificar monedas.
5. **Clasifica las monedas** según su tamaño aproximado.
6. **Dibuja los círculos detectados y muestra el valor total**.

## ▶️ Cómo ejecutar el programa

### 1. Clona el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Instala las dependencias

#### 🪟 Windows
```bash
pip install opencv-python numpy
```

#### 🍏 macOS
Primero asegúrate de tener Homebrew y Python instalado:
```bash
brew install python
pip3 install opencv-python numpy
```

#### 🐧 Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3-pip
pip3 install opencv-python numpy
```

### 3. Ejecuta el script principal

#### Windows
```bash
python main.py
```

#### macOS / Linux
```bash
python3 main.py
```

> Asegúrate de estar en el directorio del proyecto al ejecutar el script.

---

## 📷 Requisitos de las imágenes

- Las imágenes deben estar en la carpeta `IMGs_monedas/`.
- Cada imagen debe mostrar monedas mexicanas (1, 2, 5, 10 pesos) sobre una superficie con contraste.
- El script funciona mejor si las imágenes tienen una resolución razonable y fondo uniforme.

## 🛠️ Archivos importantes

| Archivo/Carpeta                  | Descripción                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `main.py`                        | Ejecuta todo el proceso de carga, detección y visualización             |
| `funciones/preprocesamiento.py` | Reduce tamaño, convierte a escala de grises y desenfoca la imagen       |
| `funciones/desenfoque_gaussiano.py` | Implementación del filtro gaussiano personalizado                    |
| `funciones/clasificacion.py`    | Clasifica las monedas detectadas según su tamaño                        |
| `IMGs_monedas/`                 | Contiene las imágenes de entrada a analizar                             |

---

## 💡 Ejemplo de salida

La consola mostrará un resumen como este:

```
Resumen de monedas detectadas:
Monedas de $1: 2
Monedas de $2: 1
Monedas de $5: 3
Monedas de $10: 1
Valor total: $28
```

Y se abrirá una ventana con los círculos dibujados sobre las monedas y el total.

---

## 🤖 Requisitos

- Python 3.7 o superior
- OpenCV
- NumPy

---

## ✨ Autores

Desarrollado por **Paulina Méndez López**  y **Gael Cumplido Mendoza**, 
Estudiantes de Ingeniería en el Tecnológico de Monterrey
