import numpy as np
import cv2

##Einlesen der Koordinaten des Mittelpunktes der BoundingBox
src = np.array([
 [737, 373],
 [747, 371],
 [792, 364],
 [832, 360],
 [844, 359],
 [881, 355],
 [892, 355],
 [914, 351],
 [924, 351],
 [936, 350],
 [955, 348],
 [964, 347],
 [973, 346],
 [992, 345],
 [1000, 344],
 [1010, 343],
 [1020, 343],
 [1036, 342],
 [1044, 342],
 [1061, 341],
 ],dtype="float32")

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
mtx = np.matrix([
    [fx,  0, cx],
    [ 0, fy, cy],
    [ 0,  0,  1]
], dtype = "float32")

distCoeff = np.array([k1, k2, p1, p2,k3], dtype = "float64")

##neueKameramatrix
new_camera_matrix = np.array([[634.80987549,   0.,         325.62947355], [ 0.,         629.81347656 ,284.07298482 ], [0., 0., 1]], dtype=np.float64)

Calibration = cv2.undistort(src,mtx,distCoeff,None,new_camera_matrix)

##Entzeichnen der Koordinaten
dst = cv2.undistortPoints(src, new_camera_matrix, distCoeff,None,new_camera_matrix)

print("\nUndistortedPoints:\n",dst)

##https://answers.opencv.org/question/230847/undistort-and-undistortpoints-are-inconsistent/
