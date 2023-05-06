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

    bordes = cv.Canny(imagen,100,200)
    cv.imshow("Camara", bordes)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
