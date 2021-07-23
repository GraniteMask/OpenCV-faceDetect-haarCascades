import cv2 as cv

img = cv.imread('lady.jpg')
cv.imshow("Lady",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

cv.waitKey(0)

#haarcascade files are taken from opencv github rep --> data