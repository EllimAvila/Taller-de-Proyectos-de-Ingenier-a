# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
"""
Se lee la imagen del directorio del proyecto
"""
imagen=cv2.imread('figuras.png')
"""
Se modifican los colores de la imagen a escala de grises
"""
grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
"""
Se binariza la imagen con la función canny
"""
bordesAislados=cv2.Canny(grises, 100, 150)
"""
Se le aplica dilatación y erosión a la imagen para facilitar su identificación
"""
bordesAislados=cv2.dilate(bordesAislados, None, iterations=1)
bordesAislados=cv2.erode(bordesAislados, None, iterations=1)
"""
Se encuentran los contornos externos de la imagen binarizada con la función findcontours

Parámetros:imagen a procesar, modo de recuperación, método de almacenamiento
"""
contornos,_=cv2.findContours(bordesAislados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
"""
Se inicia un bucle para poder trabajar con los pixeles
"""
for i in contornos:
    """
    Se determina epsilon, que es la variable para establecer la precisión 
    con la que serán dibujados los contornos
    """
    epsilon=0.01*cv2.arcLength(i, True)
    """
    Se calcula el numero de vértices de los contornos encontrados
    """
    vertices=cv2.approxPolyDP(i, epsilon, True)
    """
    Se ubica cada contorno dibujado en un área rectangular invisible
    """
    a,b,c,d=cv2.boundingRect(vertices)
    """
    Se ingresa el texto correspondiente al nombre de la figura geométrica
    tomando las coordenadas a y b como referencia
    """
    if len(vertices)==3:
        cv2.putText(imagen, 'Triangulo', (a,b-5), 1, 1, (255,0,0),1)
    """
    En el caso de las figuras de 4 lados, como podría tratarse de un 
    cuadrado o de un rectángulo son necesarios cálculos adicionales
    """
    if len(vertices)==4:
        
        """
        Se determina la relación de aspecto dividiendo las dimensiones 
        de la figura
        """
        relacionAspecto=float(c)/d
        """
        Si el resultado de la división es 1, significa que las
        dimensiones son iguales y que, por lo tanto, se trata de un cuadrado
        """
        if relacionAspecto==1:
            cv2.putText(imagen, 'Cuadrado', (a,b-5), 1, 1, (255,0,0),1)
            """
            Si esta condición no se cumple significa que la figura es un rectángulo
            """
        else:
            cv2.putText(imagen, 'Rectangulo', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==5:
        cv2.putText(imagen, 'Pentagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==6:
        cv2.putText(imagen, 'Hexagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==7:
        cv2.putText(imagen, 'Heptagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==8:
        cv2.putText(imagen, 'Octagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==9:
        cv2.putText(imagen, 'Eneagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)==10:
        cv2.putText(imagen, 'Decagono', (a,b-5), 1, 1, (255,0,0),1)
    elif len(vertices)>10:
        cv2.putText(imagen, 'Circulo', (a,b-5), 1, 1, (255,0,0),1)
    """
    Se dibujan los contornos encontrados con la función drawContours
    Parámetros:Lienzo, grupo de contornos, contorno específico a dibujar,
    color en BGR, grosor
    """    
    cv2.drawContours(imagen, [vertices],0, (255,0,0),2)#3er parámetro negativo para seleccionar todos
    """
    Mostrar imagen natural
    """
    cv2.imshow('Imagen', imagen)
    """
    Mostrar imagen en escala de grises
    """
    #cv2.imshow('Escala de grises', grises)
    """
    Mostrar imagen binarizada
    """
    #cv2.imshow('Imagen binarizada', bordesAislados)
    """
    se espera a presionar cualquier tecla antes de procesar el siguiente
    contorno
    """
    cv2.waitKey(0) & 0xFF
"""
    Una vez que se hayan mostrado todos los contornos encontrados
    se espera a presionar cualquier tecla para cerrar el programa
"""
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


