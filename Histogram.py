import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%Dış Gürültü Giderme
img = cv2.imread("klon.jpg")
b,g,r = cv2.split(img)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
