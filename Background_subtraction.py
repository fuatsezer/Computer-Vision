import cv2
import numpy as np
#%%
cap = cv2.VideoCapture("car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history = 100,varThreshold =120,detectShadows=True)

while 1:
    _,frame = cap.read()
    mask = subtractor.apply(frame)
    mask=cv2.resize(mask,(640,480))
    cv2.imshow("mask",mask)
    cv2.waitKey(20)

    
    
    
cap.release()
cv2.destroyAllWindows()