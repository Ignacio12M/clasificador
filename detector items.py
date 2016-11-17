import cv2
import numpy as np


img =  cv2.imread('WIN_20161115_11_14_43_Pro.jpg')
#tratamiento de imagen
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #transforma la imagen en escala de grises
ret,thresh = cv2.threshold(imgGray,127,255,0)      
image, contours, hierarchy = cv2.findContours(thresh,1,2)

cadena_text = ["item ",["1","2","3","4","5","6","7","8","9"]] # Esto no se deberia hacer, ya que no conoces el numero exacto de items

def cuenta(items=0):
    point= {}
    for c in contours:
        if 80<= cv2.contourArea(c) <= 10000:
            posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)  # Guardamos las dimensiones de la Bounding Box
            cv2.rectangle(img, (posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto), (0, 0, 255),2)  # Dibujamos la bounding box sobre diff1
            point[items]=[posicion_x, posicion_y, posicion_x+ancho, posicion_y+alto]
            #print point[items]
            items+=1
    return point

def texto():
    pos = cuenta()
    items = "items"
    contador = 1
    for i in pos:
        cv2.putText(img, items + contador , (pos[i][0],pos[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (11, 255, 255), 1, cv2.LINE_AA)
        contador += 1


def ventanas():
    while (1):
        cv2.imshow('therch',thresh)
        cv2.imshow('img', img)
        #cv2.imshow('transformacion', transformacion)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

    
texto()
ventanas()

