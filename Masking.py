import cv2 as cv
import numpy as np

# READING IMAGES
img = cv.imread("images/cats/3.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(
    blank, (img.shape[1] // 2, img.shape[0] // 2 - 45), 100, 255, -1
)  # The dimensions of the mask must be equal to dimensions of image.
cv.imshow("mask", mask)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weired_shape = cv.bitwise_or(mask, rectangle)


masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked", masked)


cv.waitKey(0)
