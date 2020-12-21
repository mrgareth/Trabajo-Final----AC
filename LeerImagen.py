import cv2


imagen = cv2.imread('ojito.jpeg',0)#default es 1(normal), 0(grises)
imagenColor = cv2.imread('ojito.jpeg')
cv2.imshow('Prueba de imagen',imagen)
cv2.imshow('Prueba de color',imagenColor)
cv2.imwrite('ojitoGris.png',imagen)
cv2.waitKey(0)#esta en milisegundos y el 0 significa que se cerrara al presionar cualquier tecla
cv2.destroyAllWindows()