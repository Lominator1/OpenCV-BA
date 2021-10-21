import numpy as np
import cv2
import glob

##Definition Bildgröße und Innenecken des Schachbrettmusters (Breite,Höhe)
chessboardSize = (6,8)

##Festlegung der Abbruchkriterien
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.0001)

##Vorbereitung der Objektpunkte z.B (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
##https://stackoverflow.com/questions/37310210/camera-calibration-with-opencv-how-to-adjust-chessboard-square-size
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)*20  # multiplizieren der Seitenläne des Quadrats

## Erstellung eines Arrays zum Speichern von Objektpunkten und Bildpunkten aus allen Bildern.
objpoints = []          ##3D Punkte --> Weltkoordinatensystem
imgpoints = []          ##2D Punkte --> Bildkoordinatensystem

##Durchlauf für alle Bilder mit der Endung .png/
images = glob.glob('*.png')
for image in images:
    print(image)
    img = cv2.imread(image)                         ##einlesen aller Bilder
    #img = cv2.imread ("Kalibrierung/sb6.png")      ##einlesen eines Bildes
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ##Innencken des Schachbrettmusters
    ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)


    ##Falls Innenecken gefunden --> Objekt- und Bildpunkte hinzufügen
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)            ##winsize ???
        imgpoints.append(corners)

        ##Zeichnen der Ecken
        cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv2.imshow('img', img)
        #cv2.imwrite('Resources/sb5points.jpg', img)                     # speichern des entstandenen Bildes
        cv2.waitKey(1)


####################################Verzerrung###########################################################

# mtx = Kameramatrix
# dist = Distortion (Verzerrung)
# rvecs = Rotationsvektoren
# tvec = Translationsvektoren

##Kalibrierung der Kamera
ret, cameraMatrix, distCoeff, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

##Ausgabe der Kameramatrix, Verzeichnungskoeffizienten..
print("\nCameraMatrix:\n",cameraMatrix)
print("\nVerzeichnungskoeffizienten:\n",distCoeff)

#img = cv2.imread("opencv_frame_7.png")
h,  w = img.shape[:2]
w =640
h =480
newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, distCoeff, (w,h), 0, (w,h))

##Entzeichnen
dst = cv2.undistort(img, cameraMatrix, distCoeff, newCameraMatrix)

print("\nnewCameraMatrix:\n",newCameraMatrix)


##Ausgabe des Bildes --> entzeichnet
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('caliResult1.jpg', dst)


##Ausgabe des Fehlers
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, distCoeff)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )
cv2.destroyAllWindows()