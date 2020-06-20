# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
import numpy as np
"""
Función para determinar el color
"""
def colorFigura(imagenHSV):
    """
    Definir rangos de colores
    AZUL
    """
    azulInicio=np.array([110,90,30],np.uint8)
    azulFin=np.array([126,255,255],np.uint8)
    """ROJO"""
    rojoInicio=np.array([0,90,30],np.uint8)
    rojoFin=np.array([7,255,255],np.uint8)
    """VERDE"""
    verdeInicio=np.array([40,90,30],np.uint8)
    verdeFin=np.array([75,255,255],np.uint8)
    """AMARILLO"""
    amarilloInicio=np.array([15,90,30],np.uint8)
    amarilloFin=np.array([45,255,255],np.uint8)
    """
    Se aislan los colores definidos
    """
    aislarRojo=cv2.inRange(imagenHSV, rojoInicio, rojoFin)
    aislarAzul=cv2.inRange(imagenHSV, azulInicio, azulFin)
    aislarAmarillo=cv2.inRange(imagenHSV, amarilloInicio, amarilloFin)
    aislarVerde=cv2.inRange(imagenHSV, verdeInicio, verdeFin)
    """
    Se ubican los contornos
    """
    contornosRojo=cv2.findContours(aislarRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contornosAzul=cv2.findContours(aislarAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contornosAmarillo=cv2.findContours(aislarAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contornosVerde=cv2.findContours(aislarVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    """
    Se determina el color por la cantidad de contornos encontrados 
    """
    if len(contornosRojo)>0:
        color='Rojo'
    elif len(contornosAzul)>0:
        color='Azul'
    elif len(contornosAmarillo)>0:
        color='Amarillo'
    elif len(contornosVerde)>0:
        color='verde'
    
    return color;

"""
Función para determinar el nombre de la figura
"""
def nombreFigura(contorno,base,altura):
    
    epsilon=0.01*cv2.arcLength(contorno,True)
    vertices=cv2.approxPolyDP(contorno, epsilon, True)
    
    if len(vertices)==3:
        nombre='Triangulo'
    if len(vertices)==4:
        relacionAspecto=float(c)/d
        if relacionAspecto==1:
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
    return nombre
"""Selección y preparación de la imagen para su procesamiento"""
imagen=cv2.imread('figuras2.png')
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
bordesAislados=cv2.Canny(grises, 100, 150)
bordesAislados=cv2.dilate(bordesAislados, None, iterations=1)
bordesAislados=cv2.erode(bordesAislados, None, iterations=1)
"""Preparación de parámetros para las funciones"""
contornos,_=cv2.findContours(bordesAislados, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
colorConvertido=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
for i in contornos:
    a,b,c,d=cv2.boundingRect(i)
    """Aislamiento de figura específica con color original en pantalla negra"""
    aislarFigura=np.zeros(imagen.shape[:2], dtype="uint8")
    aislarFigura=cv2.drawContours(aislarFigura,[i],-1,255,-1)
    figuraAislada=cv2.bitwise_and(colorConvertido,colorConvertido, mask= aislarFigura)
    nombre=nombreFigura(i,c,d)
    color=colorFigura(figuraAislada)
    figuraColor=nombre+' '+color
    cv2.putText(imagen, figuraColor, (a,b-5), 1, 1, (255,0,0),2)
    """Imagen natural"""
    cv2.imshow('ventana',imagen)
    cv2.waitKey(0)
"""Imagen en escala de grises"""
#cv2.imshow('grises',grises)
"""Imagen binarizada"""
#cv2.imshow('imagen binarizada',bordesAislados)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
























    