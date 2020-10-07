# Görüntüyü Gürültülerinden Kurtarma
import cv2
import numpy as np
#%%
img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")
#%%
blur = cv2.blur(img_filter,(8,8))
blur2 = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
#%%
median_blur = cv2.medianBlur(img_median,7)
#%%
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)
#%%
cv2.imshow("Blur",blur_b)
cv2.imshow("Orjinal",img_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()