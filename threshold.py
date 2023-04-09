import numpy as np
import cv2

def nothing(x):
    pass

img = cv2.imread('image_edit2.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image')

cv2.createTrackbar('th','image',0,255,nothing)
ret, thresh1 = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshed_image.jpeg',thresh1)

while True:
    th = cv2.getTrackbarPos('th', 'image')

    ret, thresh1 = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)

    cv2.imshow('image', thresh1)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyedAllWindows()
