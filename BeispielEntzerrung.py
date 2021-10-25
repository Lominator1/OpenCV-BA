import numpy as np
import cv2
import glob

img = cv2.imread("caliResult.png")

Tmatrix = np.array([[-1.52413573e-01, -2.04170172e-02, -5.52678478e+01],
                    [1.85288712e-01,  1.36431915e-01, -3.12909051e+02],
                    [1.12212573e-03, -1.20628349e-02,  1]], dtype=np.float32)



##Entzerrung --> Entzeichnetenen Koordinaten, Transformationsmatrix, dsize
Endgültige_Entzerrung = cv2.warpPerspective(img,Tmatrix,dsize=(1282,714))


#cv2.imwrite('caliResult',img)
cv2.imshow('EntzResult',Endgültige_Entzerrung)
cv2.waitKey(0)