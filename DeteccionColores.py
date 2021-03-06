import cv2
import numpy as np

captura = cv2.VideoCapture(0) #la variable que captura la cámara

while (captura.isOpened()):
    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    if ret==True:
        frameHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto sabemos que es una maquina de 64 bits
            break
        
captura.release()
cv2.destroyAllWindows()