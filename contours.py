import numpy as np
import cv2

img = cv2.imread('threshed_image_unnoised.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray,5,70,70)
contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# cv2.drawContours(img, contours, -1, (0,255,0), 2)

for contour in contours:
    if 500 < cv2.contourArea(contour) <15000:
        print(cv2.contourArea(contour))
        cv2.drawContours(img, contour, -1, (0, 255, 0), 2,cv2.LINE_AA)

cv2.imshow('Contours', img)
cv2.imwrite('contours.jpeg',img)
cv2.waitKey(0)
cv2.destroyedAllWindows()
