# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
import numpy as np

def colorFigura(imagenHSV):
    """
    Definir rangos de colores
    AZUL
    """
    azulInicio=np.array([110,90,30],np.uint8)
    azulFin=np.array([126,255,255],np.uint8)
    """VERDE"""
    verdeInicio=np.array([40,90,30],np.uint8)
    verdeFin=np.array([75,255,255],np.uint8)
 
    """
    Se aislan los colores definidos
    """
    aislarAzul=cv2.inRange(imagenHSV, azulInicio, azulFin)
    
    aislarVerde=cv2.inRange(imagenHSV, verdeInicio, verdeFin)
    """
    Se ubican los contornos
    """
    contornosAzul=cv2.findContours(aislarAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    contornosVerde=cv2.findContours(aislarVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    """
    Se determina el color por la cantidad de contornos encontrados 
    """
    
    aux = len(contornosAzul)
    if aux <= len(contornosVerde):
        aux = len(contornosVerde)
        
    if aux == len(contornosAzul):
        color='Azul'
    
    elif aux == len(contornosVerde):
        color='verde'
    
    
    return color;

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
    return nombre

def rastrearColores(aislarColor, color,fotograma,HSV):
    contornos,_=cv2.findContours(aislarColor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contornos:
        area=cv2.contourArea(i)
        if area>3000:
            i=cv2.convexHull(i)#quitar ruido
            a,b,c,d=cv2.boundingRect(i)
            aislarFigura=np.zeros(fotograma.shape[:2], dtype="uint8")
            aislarFigura=cv2.drawContours(aislarFigura,[i],-1,255,-1)
            figuraAislada=cv2.bitwise_and(HSV,HSV, mask= aislarFigura)
            nombreDelColor=colorFigura(figuraAislada) 
            nombre=nombreFigura(i,c,d) 
            figuraColor=nombre+' '+nombreDelColor
            cv2.drawContours(fotograma, [i], 0, color,3)
            cv2.putText(fotograma, figuraColor, (a,b-5), 1, 1, color,2)
            
            
"""
MAIN
"""
conexionCamara=cv2.VideoCapture(0) 

azulInicio=np.array([110,90,30],np.uint8)
azulFin=np.array([126,255,255],np.uint8)

rojoInicio=np.array([0,90,30],np.uint8)
rojoFin=np.array([7,255,255],np.uint8)

verdeInicio=np.array([40,90,30],np.uint8)
verdeFin=np.array([75,255,255],np.uint8)



while(conexionCamara.isOpened()):

    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:  #Si se reciben imágenes inicia el proceso
        """imagen HSV"""
        colorConvertido=cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        
        
        
        aislarAzul=cv2.inRange(colorConvertido, azulInicio, azulFin)
        
        aislarVerde=cv2.inRange(colorConvertido, verdeInicio, verdeFin)
        
        rastrearColores(aislarAzul, (255,0,0),fotograma,colorConvertido)
        
        rastrearColores(aislarVerde, (0,255,0),fotograma,colorConvertido)
        
        cv2.imshow('ventana', fotograma)

        if cv2.waitKey(10) & 0xFF ==ord('s'):
            break

conexionCamara.release()
cv2.destroyAllWindows()       
            
















    