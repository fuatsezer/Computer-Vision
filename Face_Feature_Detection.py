import cv2
import numpy as np
#%%
cap = cv2.VideoCapture(0)
while 1:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250,200:400]
    cv2.rectangle(frame,(250,50),(400,200),(0,0,255),2)
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)
    mask = cv2.inRange(hsv,lower_color,upper_color)
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)
    cv2.waitKey(5)
cap.release()
cv2.destroyAllWindows()
