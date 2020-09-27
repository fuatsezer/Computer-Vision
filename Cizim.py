import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255
img = cv2.resize(canvas,(1000,1000),interpolation=cv2.INTER_AREA)
"""
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
