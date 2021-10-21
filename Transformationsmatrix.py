import cv2
import numpy as np

##Passpunkte vom Tisch --> digital gemessen (Paint --> Unterschied zwischen Kamera1 und Kamera2)
src = np.array([[[1111,507],
 [792,548],
 [537,446],
 [979,393],
 [1184,447],
 [1144,387],
 [852,431],
 [934,358],
 [434,688],
 [209,485]]],np.float32)

##Passpunkte vom Tisch --> manuell gemessen
dst = np.array([[60,10],
                [40,20],
                [40,40],
                [80,30],
                [80,10],
                [100,20],
                [60,30],
                [90,40],
                [20,20],
                [20,45]],np.float32)


ergebnis = cv2.findHomography(src,dst)


print("Transformationsmatrix:",ergebnis)