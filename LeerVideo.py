import cv2

captura = cv2.VideoCapture('video.avi') #la variable que abre el video

while (captura.isOpened()):
    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    if ret==True:
        cv2.imshow('video', imagen)
        if cv2.waitKey(30) & 0xFF == ord('s'): #Si modificas el WaitKey se vera mas lento XD
            break
    else:#esto hace que se quite la ultima parte del video y no se quede abierta la ventana un while infinito sin esto
        break
captura.release()#no olvides cerrarlo
cv2.destroyAllWindows()