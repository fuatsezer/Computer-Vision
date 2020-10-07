import cv2
import numpy as np
#%%
img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img,(640,550))
img2 = cv2.imread("aircraft.jpg")
img2 = cv2.resize(img,(640,550))

if img1.shape == img2.shape:
    print("Equal Size")
else:
    print("not Equal")

diff = cv2.subtract(img1,img2)
b,g,r = cv2.split(diff)
if (cv2.countNonZero(b) == 0) & (cv2.countNonZero(g) == 0) & (cv2.countNonZero(r) == 0):
    print("completly equal")
else:
    print("not completely equal")
    

cv2.imshow("diff",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()