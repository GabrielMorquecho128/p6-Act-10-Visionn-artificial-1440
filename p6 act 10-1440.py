import numpy as np
import cv2

# Vision artificial act 10 NC 1440
# 1. Lee la imagen en escala de grises
img = cv2.imread("elcarro.jpg", cv2.IMREAD_GRAYSCALE)

if img is not None:
    # Abre la ventana con la imagen
    cv2.imshow("elcarro 1440", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Advertencia: No se pudo cargar 'elcarro.jpg'. Verifica la ruta de la imagen.")

# 2. Linea
print("La linea 1440")
# Crea una imagen negra
img = np.zeros((512, 512, 3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img, (0, 0), (511, 511), (255, 255, 255), 3)

# Abre la ventana con la imagen
cv2.imshow("Line 1440", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Circulo
# Dibuja un circulo azul de radio 10px al centro de la imagen (BGR: Azul = (255,0,0))
img = cv2.circle(img, (256, 256), 10, (255, 0, 0), -1)

# Abre la ventana con la imagen
cv2.imshow("circulo azul 1440", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Texto (Corregido: ahora se muestra la ventana)
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Example Text", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Texto 1440", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Thresholding
# 5. Thresholding
img = cv2.imread('image1.png', 0)

# Si no encuentra la imagen 'image1.png', crea una imagen de degradado para probar
if img is None:
    print("No se encontró 'image1.png'. Generando imagen de prueba temporal...")
    # Crea un degradado de 0 a 255
    img = np.tile(np.linspace(0, 255, 512, dtype=np.uint8), (300, 1))

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY', thr1)
cv2.imshow('BINARY_INV', thr2)
cv2.imshow('TRUNC', thr3)
cv2.imshow('TOZERO', thr4)
cv2.imshow('TOZERO_INV', thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 6. Trackbars
def on_trackbar(val):
    print(val)

# Crea una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'frame', 0, 255, on_trackbar)

while True:
    cv2.imshow('frame', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Tecla ESC para salir
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    img[:] = [b, g, r]  # OpenCV utiliza el formato BGR

cv2.destroyAllWindows()

print("programa realizado por marco morquecho 1440")