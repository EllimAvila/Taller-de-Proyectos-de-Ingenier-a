# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:59:23 2020

@author: TEC
"""
import cv2
import numpy as np
"""
Rangos de colores 0 - 180
"""

"""ROJO"""
rojoInicio=np.array([0,90,20],np.uint8)
rojoFin=np.array([7,200,200],np.uint8)
"""ROJO CLARO"""
rojoClaroInicio=np.array([0,201,201],np.uint8)
rojoClaroFin=np.array([7,255,255],np.uint8)
"""NARANJA"""
naranjaInicio=np.array([8,90,20],np.uint8)
naranjaFin=np.array([16,255,255],np.uint8)
"""AMARILLO"""
amarilloInicio=np.array([17,90,20],np.uint8)
amarilloFin=np.array([40,255,255],np.uint8)
"""VERDE"""
verdeInicio=np.array([41,90,20],np.uint8)
verdeFin=np.array([73,255,255],np.uint8)
"""CELESTE"""
celesteInicio=np.array([74,90,20],np.uint8)
celesteFin=np.array([110,255,255],np.uint8)  
"""AZUL"""
azulInicio=np.array([111,90,20],np.uint8)
azulFin=np.array([126,255,255],np.uint8)
"""MORADO"""
moradoInicio=np.array([127,90,20],np.uint8)
moradoFin=np.array([150,255,255],np.uint8)
"""ROSA"""
rosaInicio=np.array([151,90,20],np.uint8)
rosaFin=np.array([172,255,255],np.uint8)
# """ROJO"""
# rojoAltoInicio=np.array([173,90,20],np.uint8)
# rojoAltoFin=np.array([180,255,255],np.uint8)

"""Módulo para determinar el color de la figura encontrada"""
def colorFigura(imagenHSV):  

    """
    Se aislan los colores definidos
    """
    aislarRojo=cv2.inRange(imagenHSV, rojoInicio, rojoFin)
    aislarRojoClaro=cv2.inRange(imagenHSV, rojoClaroInicio, rojoClaroFin)
    aislarNaranja=cv2.inRange(imagenHSV,naranjaInicio, naranjaFin)
    aislarAmarillo=cv2.inRange(imagenHSV, amarilloInicio, amarilloFin)
    aislarVerde=cv2.inRange(imagenHSV, verdeInicio, verdeFin)
    aislarCeleste=cv2.inRange(imagenHSV, celesteInicio, celesteFin)
    aislarAzul=cv2.inRange(imagenHSV, azulInicio, azulFin)
    aislarMorado=cv2.inRange(imagenHSV, moradoInicio, moradoFin)
    aislarRosa=cv2.inRange(imagenHSV, rosaInicio, rosaFin)
    # aislarRojoAlto=cv2.inRange(imagenHSV, rojoAltoInicio, rojoAltoFin)
    """
    Se ubican los contornos
    """
    totalRojo=0
    totalRojoClaro=0
    totalNaranja=0
    totalAmarillo=0
    totalVerde=0
    totalCeleste=0
    totalAzul=0
    totalMorado=0
    totalRosa=0
    # totalRojoA=0
    contornosRojo=cv2.findContours(aislarRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRojo:
        area=cv2.contourArea(i)
        if area>4000:
            totalRojo=totalRojo+1
    contornosRojoClaro=cv2.findContours(aislarRojoClaro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRojoClaro:
        area=cv2.contourArea(i)
        if area>4000:
            totalRojoClaro=totalRojoClaro+1
    contornosNaranja=cv2.findContours(aislarNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosNaranja:
        area=cv2.contourArea(i)
        if area>4000:
            totalNaranja=totalNaranja+1
    contornosAmarillo=cv2.findContours(aislarAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosAmarillo:
        area=cv2.contourArea(i)
        if area>4000:
            totalAmarillo=totalAmarillo+1
    contornosVerde=cv2.findContours(aislarVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosVerde:
        area=cv2.contourArea(i)
        if area>4000:
            totalVerde=totalVerde+1
    contornosCeleste=cv2.findContours(aislarCeleste, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosCeleste:
        area=cv2.contourArea(i)
        if area>4000:
            totalCeleste=totalCeleste+1
    contornosAzul=cv2.findContours(aislarAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosAzul:
        area=cv2.contourArea(i)
        if area>4000:
            totalAzul=totalAzul+1
    contornosMorado=cv2.findContours(aislarMorado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosMorado:
        area=cv2.contourArea(i)
        if area>4000:
            totalMorado=totalMorado+1
    contornosRosa=cv2.findContours(aislarRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRosa:
        area=cv2.contourArea(i)
        if area>4000:
            totalRosa=totalRosa+1
    # contornosRojoAlto=cv2.findContours(aislarRojoAlto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # for i in contornosRojoAlto:
    #     area=cv2.contourArea(i)
    #     if area>4000:
    #         totalRojoA=totalRojoA+1
    """
    Se determina el color por la cantidad de contornos encontrados 
    """
    aux=max(totalRojo,totalRojoClaro,totalNaranja,totalAmarillo,totalVerde,totalCeleste,totalAzul,totalMorado,totalRosa)
    
    if aux==totalRojo:color='Rojo Oscuro'
    if aux==totalRojoClaro:color='Rojo Claro'
    if aux==totalNaranja:color='Naranja'
    if aux==totalAmarillo:color='Amarillo'
    if aux==totalVerde:color='Verde'
    if aux==totalCeleste:color='Celeste'
    if aux==totalAzul:color='Azul'
    if aux==totalMorado:color='Morado'
    if aux==totalRosa:color='Rosa'
    # if aux==totalRojoA:color='Rojo A'
    
    return color;
"""Módulo para determinar el nombre de la figura encontrada"""
def nombreFigura(contorno,base,altura):
    
    epsilon=0.01*cv2.arcLength(contorno,True)
    vertices=cv2.approxPolyDP(contorno, epsilon, True)
    
    if len(vertices)==3:
        nombre='Triangulo'
    if len(vertices)==4:
        relacionAspecto=float(base)/altura
        if (relacionAspecto > 0.5 and relacionAspecto <= 1.2):
            nombre='Cuadrado' 
        else:
            nombre='Rectangulo'
    elif len(vertices)==5:
        nombre='Pentagono'
    elif len(vertices)==6:
        nombre='Hexagono'
    elif len(vertices)==7:
        nombre='Heptagono'
    elif len(vertices)==8:
        nombre='Octagono'
    elif len(vertices)==9:
        nombre='Eneagono'
    elif len(vertices)==10:
        nombre='Decagono'
    elif len(vertices)>10:
        nombre='Circulo'
    return nombre;
    
"""Módulo para rastrear los colores en la imagen de la cámara"""
def rastrearColor(aislarColor, color,fotograma,HSV):
    contornos,_=cv2.findContours(aislarColor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contornos:
        area=cv2.contourArea(i)
        if area>6500:
            i=cv2.convexHull(i)#quitar ruido
            a,b,c,d=cv2.boundingRect(i)#asignar coordenadas
            aislarFigura=np.zeros(fotograma.shape[:2], dtype="uint8")#Campo negro equivalente al fotograma
            aislarFigura=cv2.drawContours(aislarFigura,[i],-1,255,-1)#Trazo del contorno en el campo negro
            figuraAislada=cv2.bitwise_and(HSV,HSV, mask= aislarFigura)#Color natural del area dentro del contorno aislado
            """Funciones para el nombre y colkr"""
            nombreDelColor=colorFigura(figuraAislada) 
            nombre=nombreFigura(i,c,d) 
            figuraColor=nombre+' '+nombreDelColor
            cv2.drawContours(fotograma, [i], 0, color,3)
            cv2.putText(fotograma, figuraColor, (a,b-5), 1, 1, color,2)

"""MAIN"""
"""
Conexión a la cámara
"""

conexionCamara=cv2.VideoCapture(0) 

while(conexionCamara.isOpened()):
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:  #Si se reciben imágenes inicia el proceso
        colorConvertido=cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        """Aislamiento de cada color"""
        aislarRojo=cv2.inRange(colorConvertido,rojoInicio,rojoFin)
        aislarRojoClaro=cv2.inRange(colorConvertido,rojoClaroInicio,rojoClaroFin)
        aislarNaranja=cv2.inRange(colorConvertido,naranjaInicio,naranjaFin)
        aislarAmarillo=cv2.inRange(colorConvertido,amarilloInicio,amarilloFin)
        aislarVerde=cv2.inRange(colorConvertido,verdeInicio,verdeFin)
        aislarCeleste=cv2.inRange(colorConvertido,celesteInicio,celesteFin)
        aislarAzul=cv2.inRange(colorConvertido,azulInicio,azulFin)
        aislarMorado=cv2.inRange(colorConvertido,moradoInicio,moradoFin)
        aislarRosa=cv2.inRange(colorConvertido,rosaInicio,rosaFin)
        # aislarRojoAlto=cv2.inRange(colorConvertido,rojoAltoInicio,rojoAltoFin)
        """Rastreo de colores"""
        rastrearColor(aislarRojo,[0,0,160],fotograma, colorConvertido)
        rastrearColor(aislarRojoClaro,[0,0,255],fotograma, colorConvertido)
        rastrearColor(aislarNaranja,[0,106,255],fotograma, colorConvertido)
        rastrearColor(aislarAmarillo,[0,195,255],fotograma, colorConvertido)
        rastrearColor(aislarVerde,[0,255,21],fotograma, colorConvertido)
        rastrearColor(aislarCeleste,[255,212,0],fotograma, colorConvertido)
        rastrearColor(aislarAzul,[255,0,0],fotograma, colorConvertido)
        rastrearColor(aislarMorado,[255,0,127],fotograma,colorConvertido)
        rastrearColor(aislarRosa,[216,0,255],fotograma, colorConvertido)
        # rastrearColor(aislarRojoAlto,[0,0,255],fotograma, colorConvertido)
        
        cv2.imshow('Lectura Webcam', fotograma)
        if cv2.waitKey(10) & 0xFF ==ord('s'):
            break
conexionCamara.release()
cv2.destroyAllWindows()

