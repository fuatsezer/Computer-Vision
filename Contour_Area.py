import cv2
import numpy as np
#%% 
img = cv2.imread("contour.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(contours[0])
area = cv2.contourArea(cnt)
print(area)

perimeter = cv2.arcLength(cnt,True)
print(perimeter)
#%%
cv2.imshow("Original",img)
cv2.imshow("Gray",gray)
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()