# 💰 Detection and Classification of Mexican Coins with OpenCV

This project uses **Python**, **OpenCV**, and **NumPy** to detect Mexican coins in images and classify their value (1, 2, 5, and 10 pesos) automatically based on the approximate size of each coin.

Link to a visual presentation of the proyect (In Spanish):
https://www.canva.com/design/DAGm5VH6KEk/ngrVRPkBPWjOlJbCG9Ijjw/edit?utm_content=DAGm5VH6KEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## 🗂️ Project Structure

```
.
├── main.py
├── README.md
├── funciones/
│   ├── classification.py
│   ├── gaussian_blur.py
│   └── preprocessing.py
└── IMGs_monedas/
    ├── monedas_1.jpg
    ├── monedas_2.jpg
    ├── monedas_3.jpg
    ├── monedas_4.jpg
    ├── monedas_5.jpg
    ├── monedas_6.jpg
    └── monedas_7.jpg

```

## 🧠 What does the program do?

1. Loads an image from the IMGs_monedas/ folder.
2. Resizes it for easier processing.
3. Converts it to grayscale and applies a Gaussian blur.
4. Detects circles using the Hough Transform to identify coins.
5. Classifies coins based on their approximate size.
6. Draws the detected circles and displays the total value.

## ▶️ How to run the program

### 1. Clone the repository
```bash
git clone https://github.com/mdzpaulina/contador-de-monedas.git
cd contador-de-monedas
```

### 2. Install dependencies

#### 🪟 Windows
```bash
pip install opencv-python
pip install numpy
```

#### 🍏 macOS
Make sure you have Homebrew and Python installed:
```bash
brew install python
pip3 install opencv-python
pip3 install numpy
```

#### 🐧 Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3-pip
pip3 install opencv-python
pip3 install numpy
```

### 3. Run the main script

#### Windows
```bash
python main.py
```

#### macOS / Linux
```bash
python3 main.py
```

Make sure you are in the project directory when running the script.

---

## 📷 Image Requirements

- Images must be stored inside the folder `IMGs_monedas/`.
- The picture should be taken approximately 10 cm from the surface.
- Each image should contain Mexican coins (1, 2, 5, 10 pesos) on a contrasting surface.
- Works best with images that have a uniform background and reasonable resolution.

## 🛠️ Key Files

| File/Folder                 | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `main.py`                        | Executes the entire process: load, detection, and visualization             |
| `funciones/preprocesamiento.py` | Resizes, converts to grayscale, and blurs the image       |
| `funciones/desenfoque_gaussiano.py` | Custom implementation of Gaussian blur                    |
| `funciones/clasificacion.py`    | Classifies detected coins based on size                        |
| `IMGs_monedas/`                 | Contains the input images to analyze                           |

---

## 💡 Example Output

The console will display a summary like this:

```
Resumen de monedas detectadas:
Monedas de $1: 2
Monedas de $2: 1
Monedas de $5: 3
Monedas de $10: 1
Valor total: $28
```

And a window will open showing the detected circles on the coins and the total value.

---

## Requirements

- Python 3.7 or higher
- OpenCV
- NumPy

---

## ✨ Authors

Developed by Paulina Méndez López and Gael Cumplido Mendoza,
Computer Science Engineering and Robotics and Digital Systems Engineering students at Tecnológico de Monterrey, Campus Guadalajara.
