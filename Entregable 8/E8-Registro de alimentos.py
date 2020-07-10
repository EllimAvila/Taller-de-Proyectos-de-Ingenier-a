# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
conexionCamara=cv2.VideoCapture(0)
while conexionCamara.isOpened():
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:
        cv2.rectangle(fotograma, (100,100), (250,250), (255,0,0),2)
        cv2.putText(fotograma, 'Dimension del objeto', (100,97), 1, 1, (255,0,0),2)
        recorte=fotograma[101:249,101:249]

        cv2.imshow('ventana', fotograma)
        # cv2.imshow('modelo', modelo)
        k=cv2.waitKey(1)
        if k == ord("c") :
                cv2.imwrite('temp_lagarto.jpg',recorte)
                cv2.imshow('recorte', recorte)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()

