import cv2
import numpy as np

# Le imagem do arquivo
image = cv2.imread('/home/jv/Desktop/m6-ec-encontro5/exemplos/0.jpg')

dataset = image

nitidez = [
    [0.0, -1.0, 0.0],
    [-1.0, 5.0, -1.0],
    [0.0, -1.0, 0.0]
    ]


teste = [[2.0, 0.0, -1.0],
        [0.0, 1.0, 0.0],
        [2.0, 0.0, -2.0]]

inversa = [[-2.0, -1.0, 0.0],
           [-1.0, 1.0, 1.0],
           [0.0, 1.0, 2.0]]

filtro = [nitidez,teste,inversa]



gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Definindo um kernel customizado
kernel = np.array(filtro[2], dtype=np.float32)
kernel_ = np.array(filtro[1], dtype=np.float32)


# Definindo um kernel customizado
kernel2 = np.array(nitidez, dtype=np.float32)



# Aplicando a convolução
filtered_dinho = cv2.filter2D(gray_image, -1, kernel2)
filtered_dinho3 = cv2.filter2D(gray_image, -1, kernel)
filtered_dinho2 = cv2.filter2D(filtered_dinho, -1, kernel)


# Display the original and images
cv2.imshow('Sem filtro', image)
cv2.imshow('Filtro teste', filtered_dinho3)
cv2.imshow('Filtro teste nitidez - teste', filtered_dinho2)
cv2.waitKey(0)
cv2.destroyAllWindows()