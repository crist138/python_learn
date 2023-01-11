import cv2
img = cv2.imread('imgs/contorno.jpg')
grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
umbral = cv2.threshold(grises,0,255,cv2.THRESH_BINARY)


# show window bien gringo yo ajhsdkjasdh asies
cv2.imshow('Imagen grises',grises)
cv2.waitKey(0)
cv2.destroyAllWindows()