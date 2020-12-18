import cv2

captura = cv2.VideoCapture(1)

while (captura.isOpened()):
    ret,imagen = captura.read()
    if ret == True:
        cv2.imshow('video', imagen)
        if cv2.waytKey(1) & 0xFF == ord('s'): #Con esto sabemos que es una maquina de 64 bits
            break
captura.release()
cv2.destroyAllWindows()