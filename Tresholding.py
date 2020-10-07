import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%
img = cv2.imread("klon.jpg",0)
cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
ret,th1 = cv2.threshold(img,190,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("klon-th1",th1)
cv2.imshow("klon-th2",th2)
cv2.imshow("klon-th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()