import cv2
import numpy as np

img =cv2.imread('Unbenannt.PNG')

##Kameramatrix Kamera1
fx = 635.80332894
fy = 639.86770768
cx = 326.13907832
cy = 288.60786999

##Verzeichnungskoeffizienten Kamera1
k1 = -4.07156698e-01
k2 = 6.85895937e-01
p1 = 4.94388122e-04
p2 = 1.78212734e-03
k3 = -1.41638566

##Übertrag in OpenCV
cameraMatrix = np.matrix([
    [fx,  0, cx],
    [ 0, fy, cy],
    [ 0,  0,  1]
], dtype = "float64")

distCoeff = np.array([k1, k2, p1, p2,k3], dtype = "float64")

##neueKameramatrix
newCameraMatrix = np.array([[634.80987549,   0. ,        325.62947355], [ 0.,         629.81347656, 284.07298482], [0., 0., 1]], dtype=np.float64)

Calibration = cv2.undistort(img,cameraMatrix,distCoeff,None,newCameraMatrix)

cv2.imwrite('caliResult.png',img)
#cv2.imshow('caliresult',img)
cv2.waitKey(0)