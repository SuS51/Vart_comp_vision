import cv2
import numpy as np

img = np.zeros((500,500,3), np.uint8)

#img[220:300,100:300] = 225,0,0
#img[:] = 225,0,0


cv2.line(img, (0,500), (500,0), (0,255,250),10)
cv2.rectangle(img, (100,100), (250,350), (0,0,255), 5 )
cv2.rectangle(img, (150,150), (200,300), (0,255,0), cv2.FILLED )
cv2.circle(img, (175,200), 20, (255,255,0), 5)


cv2.imshow("image", img)
cv2.waitKey(0)