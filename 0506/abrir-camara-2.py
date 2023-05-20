import cv2 as cv

#camara = cv.VideoCapture(cv.CAP_V4L2)
camara = cv.VideoCapture(1)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    # Agregar las siguientes 2 lineas
    espejo = cv.flip(imagen,1) # 0,1,-1
    cv.imshow("Espejo", espejo)

    cv.imshow("Camara", imagen)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
