import numpy as np
import cv2

pp = cv2.imread('image.jpeg')

img = cv2.imread('threshed_image_unnoised_smooth.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,4,5,0.23)
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
for i in range(1, len(corners)):
    print(corners[i])
img[dst>0.1*dst.max()]=[0,0,255]

for i in range(1, len(corners)):
    print(corners[i,0])
    cv2.circle(img, (int(corners[i,0]), int(corners[i,1])), 7, (0,255,0), 2)

pp = cv2.line(pp, (int(corners[3,0]), int(corners[3,1])), (int(corners[4,0]), int(corners[4,1])), (0,255,0), 5,20)
pp = cv2.line(pp, (int(corners[4,0]), int(corners[4,1])), (int(corners[2,0]), int(corners[2,1])), (0,255,0), 5,20)
pp = cv2.line(pp, (int(corners[2,0]), int(corners[2,1])), (int(corners[1,0]), int(corners[1,1])), (0,255,0), 5,20)
pp = cv2.line(pp, (int(corners[1,0]), int(corners[1,1])), (int(corners[3,0]), int(corners[3,1])), (0,255,0), 5,20)




cv2.imshow('image', pp)
cv2.imwrite('final_image2.jpeg',pp)

cv2.waitKey(0)
cv2.destroyAllWindows
