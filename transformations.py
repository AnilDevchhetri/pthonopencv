import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

cv.imshow("Main", img)


# Translation
def translate(img, x, y):
    transmet = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmet, dimensions)


# -x --> left
#  -y --> up
# X --> right
# y --> donw

translate = translate(img, 100, 100)
cv.imshow("translate", translate)

cv.waitKey(0)
