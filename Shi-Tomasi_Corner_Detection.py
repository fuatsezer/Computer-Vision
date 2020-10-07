import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%
img = cv2.imread("contour.png")
img2 = cv2.imread("text.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)
    
cv2.imshow("Corner",img),
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray2 = np.float32(gray2)
corners2 = cv2.goodFeaturesToTrack(gray2,190,0.01,10)
corners2 = np.int0(corners2)
for corner in corners2:
    x,y = corner.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)
    
cv2.imshow("Corner",img2),
cv2.waitKey(0)
cv2.destroyAllWindows()