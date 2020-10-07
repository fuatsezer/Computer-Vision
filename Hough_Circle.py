import cv2
import numpy as np
#%% 
img = cv2.imread("coins.jpg")
img2 = cv2.imread("balls.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img1_blur = cv2.medianBlur(gray,5,)
img2_blur = cv2.medianBlur(gray2,5,)
circles = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,
                           minRadius=15,maxRadius=80)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
#%%
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
