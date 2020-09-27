import cv2
import numpy as np
#%% Resimleri Okuma
img = cv2.imread("klon.jpg")
#%%
print(img)
#%% Resimleri Görme
%matplotlib auto
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
#%% Resimleri Görme
cv2.imshow("Image",img)
#%% Resimleri Kaydetme
cv2.imwrite("klon1.jpg",img)