import cv2

cam = cv2.VideoCapture(0)               #Webcam

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("sb3", frame)           #Name des Fenster
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:                     #Esc schließt Fenster
        # ESC pressed
        print("Esc hit, closing...")
        break
    if k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)        #opencv_frame_0.png written! Bild gespeichert über Leertaste
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()