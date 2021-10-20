import cv2
import numpy as np
import random
def getCountours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area >1000:
            cv2.drawContours(imgContours,contours, -1, (255,0,0), 3, cv2.LINE_4, hierarchy)
            peri = cv2.arcLength(cnt, True) #периметр
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # приблизительная кривая
            corner_count = len(approx)
            x,y, w,h =cv2.boundingRect(approx)
            if corner_count == 3:
                object_tipe = "Tri"
            elif  corner_count == 4:
                ratio = w/float(h)
                if 0.98<ratio<1.03:
                    object_tipe = "Square"
                else:
                    object_tipe = "Rect"
            elif corner_count>4: object_tipe = "Circle"
            else: object_tipe = "None"


            cv2.putText(imgContours, object_tipe, (x+20, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (), 2)


def thresh_callback(val):
    imgCanny = cv2.Canny(imgBlur,val, val)
    contours, hierarchy= cv2.findContours(imgCanny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing= np.zeros((imgCanny.shape[0],imgCanny.shape[1],3),np.uint8)
    for i in range(len(contours)):
        color = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cv2.drawContours(drawing,contours,i,color,2,cv2.LINE_8,hierarchy,0)
    cv2.imshow('Contours',drawing)

img:np.ndarray = cv2.imread('shapes.png', cv2.IMREAD_COLOR)
imgContours = img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray, (15,15),1)
imgCanny = cv2.Canny(imgBlur,150,150)
getCountours(imgCanny)


getCountours(imgBlur)
#Create Window
# window_name = 'Shape'
# cv2.namedWindow(window_name)
# cv2.imshow(window_name,img)

# max_thresh = 255
# init_thresh =100
# cv2.createTrackbar('Canny Thresh:',window_name,init_thresh,max_thresh,thresh_callback)
#thresh_callback(init_thresh)
# cv2.imshow('imgGray',imgGray)
cv2.imshow('imgContours',imgContours)
cv2.imshow('imgCanny',imgCanny)
cv2.waitKey()

