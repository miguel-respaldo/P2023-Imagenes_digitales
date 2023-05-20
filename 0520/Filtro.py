
import cv2 as cv


def hisEqulColor(img):
    ycrcb=cv.cvtColor(img,cv.COLOR_BGR2YCR_CB)
    channels=cv.split(ycrcb)
    cv.equalizeHist(channels[0],channels[0])
    cv.merge(channels,ycrcb)
    cv.cvtColor(ycrcb,cv.COLOR_YCR_CB2BGR,img)
    return img

camara = cv.VideoCapture(1)

if not camara.isOpened():
    print("No se puede abrir la camara")
    exit(1)

key = 48

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No se puede capturar la imagen de la camara")
        break
       
    k = cv.waitKey(1)
    
    if k != -1:
        key=k

    if key == 48:   # 0
        img = imagen
    elif key == 49: # 1
        img = cv.flip(imagen,1) # 0,1,-1
    elif key == 50: # 2
        img = cv.flip(imagen,0) # 0,1,-1
    elif key == 51: # 3
        img = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    elif key == 52: # 4
        img = cv.Canny(imagen,100,200)
    elif key == 53: # 5
        img = hisEqulColor(imagen)
    elif key == 27 or key == ord('q'): # ESC
        break
    else:
        img = imagen


    cv.imshow("Camara", img)
    
camara.release()
cv.destroyAllWindows()
