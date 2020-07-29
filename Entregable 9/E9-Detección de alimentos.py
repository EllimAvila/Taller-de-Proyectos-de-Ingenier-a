# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
"""
importar opencv para utilizar las herramientas de visión artificial
"""
import cv2
import numpy as np
"""
Función para buscar los alimentos en la pantalla
Parámetros:
    
nombre - Texto utilizado para concatenar el nombre de la imagen temp

fotograma- Lectura de la cámara

umbral- Cantidad numérica referente al porcentaje de coincidencia de la 
        funcion matchTemplate que debe ser superado para que el sistema 
        considere al objeto encontrado como positivo
        
color- Color empleado para el trazo del marco del objeto encontrado y el 
       texto que acompaña a este
"""
def buscarAlimento(nombre,fotograma,umbral,color):
    # Seleccinar la imagen temp a procesar mediante concatenación
    modelo=cv2.imread('temp_'+nombre+'.jpg')
    # Asignación de ancho y alto de la imagen temp
    ancho = 100
    alto=100
    umbral=umbral
    # redimencionamiento de imagen temp
    # modelo=imutils.resize(modelo, ancho)
    # # cv2.imshow('modelo', modelo)
    # alto,ancho,_=modelo.shape
    
    """
    Aplicación de la función matchTemplate para que la imagen temp
    recorra el fotograama en busca del objeto deseado
    """
    busqueda = cv2.matchTemplate(fotograma,modelo,cv2.TM_CCOEFF_NORMED)
    """
    Obtención de valores con el máximo grado de coincidencia
    """
    
    coincidencia=np.where(busqueda > 0.83)
    
    for j in zip(*coincidencia[::-1]): 
        cv2.rectangle(fotograma, j, (j[0] + ancho, j[1] + alto-20), color, 1)
    
    
    _, valorMaximo,_, posicionMaximo = cv2.minMaxLoc(busqueda)
    """
    Delimitación de coordenadas superior izquierda e inferior derecha
    """
    superiorIzquierda = posicionMaximo
    inferiorDerecha = (superiorIzquierda[0] + ancho, superiorIzquierda[1] + alto-20)
    """
    Si el máximo valor de coincidencia encontrado supera el umbral 
    establecido, se procede con el enmarcado del objeto en pantalla
    """
    if valorMaximo > umbral:
        cv2.rectangle(fotograma, (superiorIzquierda[0],superiorIzquierda[1]+ 6), inferiorDerecha, color, 3)
        cv2.putText(fotograma, nombre, (superiorIzquierda[0],superiorIzquierda[1]-15), 2, 1, color,2)
    
    
"""MAIN"""
# Conexión con la cámara
conexionCamara=cv2.VideoCapture(0)
# bucle para recepción de fotogramas
while conexionCamara.isOpened():
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:
        """
        Instancias del procedimiento buscarFruta
        """
        """Limón"""
        buscarAlimento('limon', fotograma, 0.7, (0,240,0))
        """Plátano"""
        buscarAlimento('platano', fotograma, 0.7, (0,154,255))
        """Mandarina"""
        buscarAlimento('mandarina', fotograma, 0.75, (0,81,250))
        """Atún"""
        buscarAlimento('atun', fotograma, 0.7, (255,0,0))
    
        """Muestra de resultados"""
        cv2.imshow('ventana', fotograma)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()