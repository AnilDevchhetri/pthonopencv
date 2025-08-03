import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")


cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

canny = cv.Canny(img, 125, 175)

cv.imshow("Canny", canny)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.waitKey(0)
