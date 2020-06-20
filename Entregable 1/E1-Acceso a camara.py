# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
"""
Primero se importan las librerias numpy para el manejo de arrays
 y cv2 para el acceso a la cámara
"""
import cv2         
"""
Ahora se abre una conexión a la cámara con el parámetro 0 para definir a la
webcam como origen
"""
conexionCamara=cv2.VideoCapture(0) 
"""
Se inicia un bucle infinito para el envio constante de fotogramas
"""
while(conexionCamara.isOpened()):
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:  #Si se reciben imágenes inicia el proceso
        """Se muestran los fotogramas en una ventana llamada "Lectura Webcam" """
        cv2.imshow('Lectura Webcam', fotograma)
        """se establece una tecla para cerrar el bucle"""
        if cv2.waitKey(1) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()
    
