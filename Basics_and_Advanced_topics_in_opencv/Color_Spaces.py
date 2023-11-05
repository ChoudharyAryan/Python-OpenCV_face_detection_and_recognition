import cv2 as cv

# import matplotlib.pyplot as plt

img = cv.imread("images/cats/2.jpg")
cv.imshow("img", img)

image = cv.imread("images/cats/3.jpg")
cv.imshow("image", image)

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to HLS
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow("hls", hls)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# # Grayscale to BGR
# gray_bgr = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
# cv.imshow("gray_bgr", gray_bgr) Can we not convert a grayscale image to BGR image?

cv.waitKey(0)
