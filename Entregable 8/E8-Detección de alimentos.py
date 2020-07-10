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
"""
importar imutils para el redimensionamiento de imágenes
"""
import imutils
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
def buscarFruta(nombre,fotograma,umbral,color):
    # Seleccinar la imagen temp a procesar mediante concatenación
    modelo=cv2.imread('temp_'+nombre+'.jpg')
    # Asignación de ancho y alto de la imagen temp
    ancho = 150
    alto=150
    # redimencionamiento de imagen temp
    modelo=imutils.resize(modelo, ancho)
    """
    Aplicación de la función matchTemplate para que la imagen temp
    recorra el fotograama en busca del objeto deseado
    """
    busqueda = cv2.matchTemplate(fotograma,modelo,cv2.TM_CCOEFF_NORMED)
    """
    Obtención de valores con el máximo grado de coincidencia
    """
    _, max_val,_, max_loc = cv2.minMaxLoc(busqueda)
    """
    Delimitación de coordenadas superior izquierda e inferior derecha
    """
    top_left = max_loc
    bottom_right = (top_left[0] + ancho, top_left[1] + alto-20)
    # establecimiento del umbral de coincidencia
    umbral=umbral
    """
    Si el máximo valor d ecoincidencia encontrado supera el umbral 
    establecido, se procede con el enmarcado del objeto en pantalla
    """
    if max_val > umbral:
        cv2.rectangle(fotograma, (top_left[0],top_left[1]+ 6), bottom_right, color, 3)
        cv2.putText(fotograma, nombre, top_left, 2, 1, color,2)

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
        """limones"""
        buscarFruta('manzana',fotograma,0.7,(0,0,255))
        cv2.waitKey(1)
        """mandarinas"""
        buscarFruta('mandarina',fotograma,0.7,(27,119,255))
        cv2.waitKey(1)
        """platano"""
        buscarFruta('platano',fotograma,0.7,(20,152,188))
        cv2.waitKey(1)
        """Muestra de resultados"""
        cv2.imshow('ventana', fotograma)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()