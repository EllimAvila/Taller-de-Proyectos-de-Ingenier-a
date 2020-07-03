# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
import imutils

conexionCamara=cv2.VideoCapture(0)
modelo=cv2.imread('temp_'+'limon'+'.jpg')
ancho = 150
alto=150
modelo=imutils.resize(modelo, ancho)
w = modelo.shape[1]
h = modelo.shape[0]
while conexionCamara.isOpened():
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:
        busqueda = cv2.matchTemplate(fotograma,modelo,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(busqueda)
        top_left = max_loc
        umbral=0.5
        if max_val > umbral:
            bottom_right = (top_left[0] + ancho, top_left[1] + alto-20)
            cv2.rectangle(fotograma, top_left, bottom_right, (255, 0, 0), 2)
            cv2.putText(fotograma, 'Aqui', (top_left), 1, 1, (255,0,0),2)

        cv2.imshow('ventana', fotograma)
        cv2.imshow('modelo', modelo)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()