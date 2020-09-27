import cv2 
#%% Webcamden video okuma
cap = cv2.VideoCapture(0)
while True:
     ret , frame = cap.read()
     frame = cv2.flip(frame,1)
     cv2.imshow("Webcam",frame)
     cv2.waitKey(30)
cap.release()
cv2.destroyAllWindows()
#%% Bilgisayardan video okuma
cap = cv2.VideoCapture("antalya.mp4")     
while True:
     ret , frame = cap.read()
     if ret == 0 :
         break
     cv2.imshow("Antalya",frame)
     cv2.waitKey(100)
