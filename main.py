import cv2
import numpy as np

img: np.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)
h,w, _ =img.shape
img = cv2.resize(img, (w//2,h//2),cv2.INTER_NEAREST)
print(type(img))
print(img.shape)

b,g,r = cv2.split(img)
#cv2.imshow('blue', b)
#cv2.imshow('green', g)
#cv2.imshow('red', r)

merge_img = cv2.merge([b,g,r])
#cv2.imshow('merge_img',merge_img)

gray_img = cv2.imread('robot.jpeg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('gray_img',gray_img)
img_height, img_width, _ =img.shape
filled_img = img.copy()
print(img_height, img_width)
for i in range(img_height//2, img_height):
    for j in range(img_width//2, img_width):
        filled_img[i,j] = (0,0,150)
cv2.imshow('color', img)
# cv2.imshow('filled_img', filled_img)
#croped_img = img[100:200, 790:900] обрезаем изоб.
#cv2.imshow('croped_igm', croped_img)
#cv2.imwrite('croped_igm.jpeg', croped_img)

img_blur = cv2.blur(img, (3,3))
img_blur7 = cv2.blur(img, (7,7))
img_blur11 = cv2.blur(img, (11,11))
cv2.imshow('blur', img_blur)
cv2.imshow('blur7', img_blur7)
cv2.imshow('blur11', img_blur11)

cv2.waitKey(0)