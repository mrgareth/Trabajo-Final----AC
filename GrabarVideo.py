import cv2

captura = cv2.VideoCapture(0) #la variable que captura la cámara
salida = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))  

while (captura.isOpened()):
    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    if ret==True:
        cv2.imshow('video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto haremos que termine al presionar 's'
            break
        
captura.release()
salida.release()
cv2.destroyAllWindows()