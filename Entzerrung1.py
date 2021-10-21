import cv2
import numpy as np

#img = cv2.imread("kamera1.PNG")

Tmatrix = np.array([[-1.52413573e-01, -2.04170172e-02, -5.52678478e+01],
                    [1.85288712e-01,  1.36431915e-01, -3.12909051e+02],
                    [1.12212573e-03, -1.20628349e-02,  1]], dtype=np.float32)

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
 [1061, 341]], dtype="float32")



##Entzerrung --> Entzeichnetenen Koordinaten, Transformationsmatrix, dsize
Endgültige_Entzerrung = cv2.perspectiveTransform(src,Tmatrix)


print("Entzerrte Punkte:",Endgültige_Entzerrung)