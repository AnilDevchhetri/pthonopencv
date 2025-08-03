import cv2 as cv


img = cv.imread("Photos/park.jpg")
cv.imshow("Boston", img)


# BGr to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscal", gray)

# BGR to HSV


cv.waitKey(0)
