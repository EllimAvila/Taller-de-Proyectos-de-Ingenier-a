# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""

import numpy as np 
import cv2         

def rastrearColores(aislarColor, color):
    contornos,_=cv2.findContours(aislarColor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contornos:
        area=cv2.contourArea(i)
        if area>3000:
             quitarRuido=cv2.convexHull(i)
             cv2.drawContours(fotograma, [quitarRuido], 0, color,3)
           # cv2.drawContours(fotograma, [i], 0, color,3)


conexionCamara=cv2.VideoCapture(0) 

azulInicio=np.array([110,90,30],np.uint8)
azulFin=np.array([126,255,255],np.uint8)

rojoInicio=np.array([0,90,30],np.uint8)
rojoFin=np.array([7,255,255],np.uint8)

verdeInicio=np.array([40,90,30],np.uint8)
verdeFin=np.array([75,255,255],np.uint8)

amarilloInicio=np.array([15,90,30],np.uint8)
amarilloFin=np.array([45,255,255],np.uint8)


while(conexionCamara.isOpened()):

    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:  #Si se reciben imágenes inicia el proceso
        
        colorConvertido=cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        aislarRojo=cv2.inRange(colorConvertido, rojoInicio, rojoFin)
        aislarAzul=cv2.inRange(colorConvertido, azulInicio, azulFin)
        aislarAmarillo=cv2.inRange(colorConvertido, amarilloInicio, amarilloFin)
        aislarVerde=cv2.inRange(colorConvertido, verdeInicio, verdeFin)
        rastrearColores(aislarRojo, (0,0,255))
        rastrearColores(aislarAzul, (255,0,0))
        rastrearColores(aislarAmarillo, (0,255,255))
        rastrearColores(aislarVerde, (0,255,0))
        cv2.imshow('ventana', fotograma)
        
        if cv2.waitKey(1) & 0xFF ==ord('s'):
            break

conexionCamara.release()
cv2.destroyAllWindows()