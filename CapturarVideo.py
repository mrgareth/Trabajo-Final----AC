import cv2

captura = cv2.VideoCapture(0) #la variable que captura la cámara

while (captura.isOpened()):
    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    if ret==True:
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto haremos que termine al presionar 's'
            break
captura.release()
cv2.destroyAllWindows()