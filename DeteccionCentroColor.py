import cv2
import numpy as np

def centro (mask, color):
    _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #AQUI capturamos la variable contornos
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000: #Esto imprimira el contorno mientras sea el area mayor a 3000
            M = cv2.moments(c)
            if(M["m00"] == 0): M["m00"] = 1
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])                     
            nuevoContorno = cv2.convexHull(c)
            cv2.circle(frame,(x, y), 7, (0, 255, 0), -1)
            cv2.putText(frame, {'',''}.format(x, y), (x+10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.drawContours(imagen, [nuevoContorno], 0, color, 3)

captura = cv2.VideoCapture(0)

amarilloBajo = np.array([15, 100, 20],np.uint8)
amarilloAlto = np.array([45, 255, 255],np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX 

while True:
    ret,frame = captura.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskAmarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
        centro(maskAmarillo, (0, 255, 255))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'): #Con esto sabemos que es una maquina de 64 bits
            break
        
captura.release()
cv2.destroyAllWindows()