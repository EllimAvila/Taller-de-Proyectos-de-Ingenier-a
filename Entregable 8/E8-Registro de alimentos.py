# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
"""
libreriá de opencv
"""
import cv2
"""
Conexión a la camara
"""
conexionCamara=cv2.VideoCapture(0)
"""
bucle para recepción de fotogramas
"""
while conexionCamara.isOpened():
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:
        """
        Enmarcado del área donde se sacará el patrón(imagen temp)
        """
        cv2.rectangle(fotograma, (100,100), (250,250), (255,0,0),2)
        cv2.putText(fotograma, 'Dimension del objeto', (100,97), 1, 1, (255,0,0),2)
        """
        Delimitación del área a recortar
        """
        recorte=fotograma[103:249,103:249]
        """
        Mostrar el fotograma
        """
        cv2.imshow('ventana', fotograma)
        # cv2.imshow('modelo', modelo)
        k=cv2.waitKey(1)
        """
        Si se presiona la tecla C se ejecuta la sentencia condicional
        """
        if k == ord("c") :
                """
                Se guarda la captura 
                """
                cv2.imwrite('temp_platano.jpg',recorte)
                """Se muestra la captura obtenida"""
                cv2.imshow('recorte', recorte)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()

