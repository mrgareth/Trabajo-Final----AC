import cv2
import numpy as np

captura = cv2.VideoCapture(0) #la variable que captura la cámara

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

while (True):

    ret,imagen = captura.read() #ret puede ser True o False y imagen seria la captura
    
    if ret==True:

        frameHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange( frameHSV, azulBajo, azulAlto)

        _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #AQUI capturamos la variable contornos
        #cv2.drawContours(imagen, contornos, -1, (255, 0, 0), 3) #Aqui dibujaremos todos los contornos en el video
        
        for c in contornos:
            area = cv2.contourArea(c)
                if area > 3000: #Esto imprimira el contorno mientras sea el area mayor a 3000
                    nuevoContorno = cv2.convexHull(c)
                    cv2.drawContours(imagen, nuevoContorno, 0, (255, 0, 0), 3)
        
        #cv2.imshow('Mascara de azul', mask) #Muestra la mascara de red en blanco 
        cv2.imshow('video', imagen)

        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto sabemos que es una maquina de 64 bits
            break
        
captura.release()
cv2.destroyAllWindows()