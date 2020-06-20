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
import numpy as np 
import cv2         

"""
Ahora se abre una conexión a la cámara con el parámetro 0 para definir a la
webcam como origen
"""
conexionCamara=cv2.VideoCapture(0) 
"""
Se define, mediante arrays, el rango en modelo HSV en el que se encuentra el 
color deseado
"""
"""AZUL"""
#inicio=np.array([110,90,30],np.uint8)
#fin=np.array([126,255,255],np.uint8)
"""ROJO OSCURO"""
inicio=np.array([0,90,20],np.uint8)
fin=np.array([7,200,200],np.uint8)
"""ROJO CLARO"""
inicio=np.array([0,201,201],np.uint8)
fin=np.array([7,255,255],np.uint8)
# """ROJO OSCURO"""
# inicio=np.array([5,180,150],np.uint8)
# fin=np.array([7,255,255],np.uint8)
"""VERDE"""
# inicio=np.array([40,90,30],np.uint8)
# fin=np.array([75,255,255],np.uint8)
"""AMARILLO"""
#inicio=np.array([21,90,30],np.uint8)
#fin=np.array([40,255,255],np.uint8)

"""
Se inicia un bucle infinito para el envio constante de fotogramas
"""
while(conexionCamara.isOpened()):

    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:  #Si se reciben imágenes inicia el proceso
        """convertir formato de color de BGR a HSV"""
        colorConvertido=cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        """Se aisla el color dentro de los rangos definidos al principio"""
        
        aislarColor=cv2.inRange(colorConvertido, inicio, fin)
        """Se configura el bloque de pixeles aislado para mostrarse con su color
        original"""
        colorAislado=cv2.bitwise_and(fotograma,fotograma, mask= aislarColor)
        """Se muestran 2 ventanas, la primera muestra la lectura original de la webcam
        y la segunda muestra los colores aislados"""
        #cv2.imshow('Color Aislado2', aislarColor)
        cv2.imshow('Color Aislado', colorAislado)
        cv2.imshow('ventana', fotograma)
        """se establece una tecla para cerrar el bucle"""
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()