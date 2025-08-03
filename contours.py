import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")

cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)


blank = np.zeros(img.shape, dtype="uint8")
# cv.imshow("blankImage", blank)

blur = cv.GaussianBlur(
    gray,
    (
        5,
        5,
    ),
    cv.BORDER_DEFAULT,
)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)


ret, thresh = cv.threshold(gray, 124, 255, cv.THRESH_BINARY)

cv.imshow("Thresh image", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found.")


cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contwres draw", blank)

cv.waitKey(0)
