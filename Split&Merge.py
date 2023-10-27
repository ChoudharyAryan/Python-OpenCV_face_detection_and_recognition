import cv2 as cv
import numpy as np

img = cv.imread("images/cats/2.jpg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# Spliting the image
b, g, r = cv.split(img)  # spliting the image into its respective color chanels.

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)


# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging the image
merged = cv.merge([b, g, r])
cv.imshow("merged", merged)


cv.waitKey(0)
