import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%Dış Gürültü Giderme
img = cv2.imread("klon.jpg",0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel,)
cv2.imshow("eresion",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%İç Gürültü Giderme
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,)
cv2.imshow("eresion",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()