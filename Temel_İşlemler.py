import cv2
import numpy as np
#%%
img = cv2.imread("klon.jpg")
dimension = img.shape
print(dimension)
color = img[205,250]
print("BGR:",color)
blue = img[420,500,0]
#%%

cv2.imshow("Klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

