import numpy as np
import cv2

def nothing(x):
    pass

img = cv2.imread('image_edit.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image')

cv2.createTrackbar('first','image',0,255,nothing)
cv2.createTrackbar('second','image',0,255,nothing)
cv2.createTrackbar('th','image',0,255,nothing)

# img = cv2.bitwise_not(img)

while True:
    first = cv2.getTrackbarPos('first', 'image')
    second = cv2.getTrackbarPos('second', 'image')
    th = cv2.getTrackbarPos('th', 'image')

    img = cv2.imread('image_edit.jpeg',0)

    edges = cv2.Canny(img, first, second,L2gradient = True)

    lines = cv2.HoughLinesP(edges, cv2.HOUGH_PROBABILISTIC, theta=1 * np.pi / 180, threshold=th, minLineLength=100, maxLineGap=10)

    if lines is not None:
        for i in lines:
            x1, y1, x2, y2 = i[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyedAllWindows()
