import cv2
import numpy as np

img = cv2.imread('pituko.JPG')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7,7),0) #Aplicar Blur
(T, bin) = cv2.threshold(suave, 160,255,cv2.THRESH_BINARY)
resultado = np.vstack([
    np.hstack([suave,bin])
])
cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)