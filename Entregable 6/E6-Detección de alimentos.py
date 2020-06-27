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
naranjaFin=np.array([16,200,200],np.uint8)
"""NARANJA CLARO"""
naranjaClaroInicio=np.array([8,201,201],np.uint8)
naranjaClaroFin=np.array([16,255,255],np.uint8)
"""AMARILLO"""
amarilloInicio=np.array([15,100,20],np.uint8)
amarilloFin=np.array([45,255,255],np.uint8)
"""VERDE"""
verdeInicio=np.array([41,90,20],np.uint8)
verdeFin=np.array([73,255,255],np.uint8)
"""CELESTE"""
celesteInicio=np.array([74,90,20],np.uint8)
celesteFin=np.array([110,255,255],np.uint8)  
"""AZUL"""
azulInicio=np.array([111,90,20],np.uint8)
azulFin=np.array([126,200,200],np.uint8)
"""AZUL CLARO"""
azulClaroInicio=np.array([111,201,201],np.uint8)
azulClaroFin=np.array([126,255,255],np.uint8)
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
    aislarNaranjaClaro=cv2.inRange(imagenHSV,naranjaClaroInicio,naranjaClaroFin)
    aislarAmarillo=cv2.inRange(imagenHSV, amarilloInicio, amarilloFin)
    aislarVerde=cv2.inRange(imagenHSV, verdeInicio, verdeFin)
    aislarCeleste=cv2.inRange(imagenHSV, celesteInicio, celesteFin)
    aislarAzul=cv2.inRange(imagenHSV, azulInicio, azulFin)
    aislarAzulClaro=cv2.inRange(imagenHSV,azulClaroInicio,azulClaroFin)
    aislarMorado=cv2.inRange(imagenHSV, moradoInicio, moradoFin)
    aislarRosa=cv2.inRange(imagenHSV, rosaInicio, rosaFin)
    # aislarRojoAlto=cv2.inRange(imagenHSV, rojoAltoInicio, rojoAltoFin)
    """
    Se ubican los contornos
    """
    totalRojo=0
    totalRojoClaro=0
    totalNaranja=0
    totalNaranjaClaro=0
    totalAmarillo=0
    totalVerde=0
    totalCeleste=0
    totalAzul=0
    totalAzulClaro=0
    totalMorado=0
    totalRosa=0
    # totalRojoA=0
    contornosRojo=cv2.findContours(aislarRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRojo:
        area=cv2.contourArea(i)
        if area>2000:
            totalRojo=totalRojo+1
    contornosRojoClaro=cv2.findContours(aislarRojoClaro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRojoClaro:
        area=cv2.contourArea(i)
        if area>2000:
            totalRojoClaro=totalRojoClaro+1
    contornosNaranja=cv2.findContours(aislarNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosNaranja:
        area=cv2.contourArea(i)
        if area>2000:
            totalNaranja=totalNaranja+1
    contornosNaranjaClaro=cv2.findContours(aislarNaranjaClaro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosNaranjaClaro:
        area=cv2.contourArea(i)
        if area>2000:
            totalNaranjaClaro=totalNaranjaClaro+1
    contornosAmarillo=cv2.findContours(aislarAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosAmarillo:
        area=cv2.contourArea(i)
        if area>2000:
            totalAmarillo=totalAmarillo+1
    contornosVerde=cv2.findContours(aislarVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosVerde:
        area=cv2.contourArea(i)
        if area>2000:
            totalVerde=totalVerde+1
    contornosCeleste=cv2.findContours(aislarCeleste, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosCeleste:
        area=cv2.contourArea(i)
        if area>2000:
            totalCeleste=totalCeleste+1
    contornosAzul=cv2.findContours(aislarAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosAzul: 
        area=cv2.contourArea(i)
        if area>2000:
            totalAzul=totalAzul+1
    contornosAzulClaro=cv2.findContours(aislarAzulClaro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosAzulClaro:
        area=cv2.contourArea(i)
        if area>2000:
            totalAzulClaro=totalAzulClaro+1
    contornosMorado=cv2.findContours(aislarMorado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosMorado:
        area=cv2.contourArea(i)
        if area>2000:
            totalMorado=totalMorado+1
    contornosRosa=cv2.findContours(aislarRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for i in contornosRosa:
        area=cv2.contourArea(i)
        if area>2000:
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
    if aux==totalNaranjaClaro:color='Naranja Claro'
    if aux==totalAmarillo:color='Amarillo'
    if aux==totalVerde:color='Verde'
    if aux==totalCeleste:color='Celeste'
    if aux==totalAzul:color='Azul'
    if aux==totalAzulClaro:color='Azul Claro'
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
            nombre=4 
        else:
            nombre='Rectangulo'
    elif len(vertices)==5:
        nombre=5
    elif len(vertices)==6:
        nombre=6
    elif len(vertices)==7:
        nombre=7
    elif len(vertices)==8:
        nombre=8
    elif len(vertices)==9:
        nombre=9
    elif len(vertices)==10:
        nombre=10
    elif len(vertices)>10:
        nombre=11
    
    
    return nombre;

"""Modulo para determinar frutas"""
def fruta(lados,color):
    nfruta ='Desconocido'
    if lados <= 9 and color=='Amarillo':
        nfruta='Platano'
    elif lados > 9 and color=='Verde':
        nfruta='Limon'
    elif lados > 9 and color=='Amarillo':
        nfruta='Limon'
    else:
        nfruta='Desconocido'
    return nfruta

"""Módulo para rastrear los colores en la imagen de la cámara"""
def rastrearColor(aislarColor, color,fotograma,HSV):
    # aislarColor=cv2.medianBlur(aislarColor, 7)
    contornos,_=cv2.findContours(aislarColor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contornos:
        area=cv2.contourArea(i)
        if area>2000:
            i=cv2.convexHull(i)#quitar ruido
            
            a,b,c,d=cv2.boundingRect(i)#asignar coordenadas
            aislarFigura=np.zeros(fotograma.shape[:2], dtype="uint8")#Campo negro equivalente al fotograma
            aislarFigura=cv2.drawContours(aislarFigura,[i],-1,255,-1)#Trazo del contorno en el campo negro
            figuraAislada=cv2.bitwise_and(HSV,HSV, mask= aislarFigura)#Color natural del area dentro del contorno aislado
            """Funciones para el nombre y color"""
            nombreDelColor=colorFigura(figuraAislada) 
            nombre=nombreFigura(i,c,d) 
            # figuraColor=nombre+' '+nombreDelColor
            nombrefruta=fruta(nombre, nombreDelColor)
            cv2.drawContours(fotograma, [i], 0, color,3)
            cv2.putText(fotograma, nombrefruta, (a,b-5), 1, 1, color,2)



"""MAIN"""
conexionCamara=cv2.VideoCapture(0)
fondo=None

while conexionCamara.isOpened():
    recibe,fotograma=conexionCamara.read()#Se obtienen lecturas de la webcam
    if recibe==True:
        preFondo=fotograma.copy()
        
        if fondo is not None:
            # cv2.imshow('fondo', fondo)
            areaTrabajo = fotograma[50:300,40:300]
            areaTrabajoGrises = cv2.cvtColor(areaTrabajo, cv2.COLOR_BGR2GRAY)
            fondoAreaTrabajo = fondo[50:300,40:300]
            cv2.rectangle(fotograma, (40-2,50-2), (300+2, 300+2), (255,0,0),2)
            
            # cv2.imshow('area',areaTrabajo)
            # cv2.imshow('AREA GRIS',areaTrabajoGrises)
            # cv2.imshow('fondo Area Gris', fondoAreaTrabajo)
            
            quitarFondo=cv2.absdiff(areaTrabajoGrises,fondoAreaTrabajo)
            areaTrabajoBinarizada=cv2.threshold(quitarFondo, 25, 255, cv2.THRESH_BINARY)[1]
            areaTrabajoBinarizada=cv2.medianBlur(areaTrabajoBinarizada, 7)
            cv2.imshow('sin fondo',quitarFondo)
            cv2.imshow('binarizado sin fondo',areaTrabajoBinarizada)
            
            colorConvertido=cv2.cvtColor(areaTrabajo, cv2.COLOR_BGR2HSV)
            
            # aislarRojoAlto=cv2.inRange(colorConvertido,rojoAltoInicio,rojsoAltoFin)
            """Aislamiento de cada color"""
            aislarRojo=cv2.inRange(colorConvertido,rojoInicio,rojoFin)
            aislarRojoClaro=cv2.inRange(colorConvertido,rojoClaroInicio,rojoClaroFin)
            aislarNaranja=cv2.inRange(colorConvertido,naranjaInicio,naranjaFin)
            aislarNaranjaClaro=cv2.inRange(colorConvertido,naranjaClaroInicio,naranjaClaroFin)
            aislarAmarillo=cv2.inRange(colorConvertido,amarilloInicio,amarilloFin)
            aislarVerde=cv2.inRange(colorConvertido,verdeInicio,verdeFin)
            aislarCeleste=cv2.inRange(colorConvertido,celesteInicio,celesteFin)
            aislarAzul=cv2.inRange(colorConvertido,azulInicio,azulFin)
            aislarAzulClaro=cv2.inRange(colorConvertido,azulClaroInicio,azulClaroFin)
            aislarMorado=cv2.inRange(colorConvertido,moradoInicio,moradoFin)
            aislarRosa=cv2.inRange(colorConvertido,rosaInicio,rosaFin)
            # aislarRojoAlto=cv2.inRange(colorConvertido,rojoAltoInicio,rojoAltoFin)
            """Rastreo de colores"""
            rastrearColor(aislarRojo,[0,0,160],areaTrabajo, colorConvertido)
            rastrearColor(aislarRojoClaro,[0,0,255],areaTrabajo, colorConvertido)
            rastrearColor(aislarNaranja,[0,86,216],areaTrabajo, colorConvertido)
            rastrearColor(aislarNaranjaClaro,[38,124,255],areaTrabajo,colorConvertido)
            rastrearColor(aislarAmarillo,[0,195,255],areaTrabajo, colorConvertido)
            rastrearColor(aislarVerde,[0,255,21],areaTrabajo, colorConvertido)
            rastrearColor(aislarCeleste,[255,255,0],areaTrabajo, colorConvertido)
            rastrearColor(aislarAzul,[255,0,0],areaTrabajo, colorConvertido)
            rastrearColor(aislarAzulClaro, [255,95,63], areaTrabajo, colorConvertido)
            rastrearColor(aislarMorado,[255,0,127],areaTrabajo,colorConvertido)
            rastrearColor(aislarRosa,[216,0,255],areaTrabajo, colorConvertido)
            # cv2.imshow('area HSV', colorConvertido)
            
        cv2.imshow('ventana', fotograma)
        k=cv2.waitKey(1)
        if k == ord("f") :
                fondo=cv2.cvtColor(preFondo, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(20) & 0xFF ==ord('s'):
            break
"""se cierran las ventanas creadas y la conexión con la webcam"""
conexionCamara.release()
cv2.destroyAllWindows()















