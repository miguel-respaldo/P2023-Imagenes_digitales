import cv2 as cv

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

    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    cv.imshow("Camara", grises)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
