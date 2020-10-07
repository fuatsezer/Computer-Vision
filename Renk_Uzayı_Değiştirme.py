import cv2
#%%
img = cv2.imread("klon.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#%%
cv2.imshow("Klon",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
