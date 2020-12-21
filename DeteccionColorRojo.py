import cv2
import numpy as np

captura = cv2.VideoCapture(0) #la variable que captura la cámara

redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

while (captura.isOpened()):
    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    if ret==True:
        frameHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1,maskRed2)

        cv2.imshow('Mascara de red', maskRed)
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto sabemos que es una maquina de 64 bits
            break
        
captura.release()
cv2.destroyAllWindows()