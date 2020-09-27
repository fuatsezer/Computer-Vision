import cv2
import numpy as np
%matplotlib auto
#%% Resimleri Okuma
img = cv2.imread("klon.jpg")
#%%
cv2.namedWindow("Klon",cv2.WINDOW_NORMAL)
cv2.imshow("Klon",img)
#%% Yeniden Boyutlandırma
img = cv2.resize(img,(640,480))
#%% Aspect ratio
def resizewithAspectRatio(img,width = None,height = None,inter = cv2.INTER_AREA):
    dimension = None
    (h,w) = img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w*r),height)
    else:
        r = width / float(w)
        dimension = (width,int(h*r))
    return cv2.resize(img,dimension,interpolation = inter)
img = cv2.imread("klon.jpg")
img1 = resizewithAspectRatio(img,height = 600)
cv2.imshow("Original",img)    
cv2.imshow("Resized",img1)  