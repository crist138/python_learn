import cv2
img = cv2.imread('imgs/monedas.jpg')
grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,0,255,cv2.THRESH_BINARY)
contorno,jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contorno,-1,(53, 171, 85),3)

# show window bien gringo yo ajhsdkjasdh asies
cv2.imshow('Show',img)
#cv2.imshow('Imagen grises',grises)
cv2.waitKey(0)
cv2.destroyAllWindows()