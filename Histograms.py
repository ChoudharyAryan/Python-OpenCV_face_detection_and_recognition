# Histograms allow you to visualize the distribution of pixel intensities in an image weather it's a grayscale image or RGB image .
# You cam visiualize these pixel intensities distribution with the help of histogram which is a kind of graph or plot.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/cats/3.jpg")
cv.imshow("img", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
# cv.imshow("mask", mask)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)

# Grayscale Histogram
# gray_histogram = cv.calcHist(
#     [gray], [0], mask, [256], [0, 256]
# )  # this functions is used to calculate the histograms of images.It takes in the parameters like listt of images ,channels,mask ,range of all possible pixil values.
# It returns  an array of histogram points of datatype float32.

# Ploting
# To ploat this histogram we are going to usr Matplotlib
# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel(
#     "Bins"
# )  # when we draw a histogram the first step is to bin the range of values- that is divide the entire range of values into a series of intervals .These are specified as conscutive non-overlaping intervals of variables.
# plt.ylabel("# of pixels")
# plt.plot(gray_histogram)
# plt.xlim(0, 256)
# plt.show()


# COLOURED HISTOGRAM
plt.figure()
plt.title("Colour Histogram")
plt.ylabel("# of pixels")
plt.xlabel("Bins")

colors = ("b", "g", "r")
for i, col in enumerate(
    colors
):  # as i understands it i contains the index of all the elements and col contains all the values if col not definec i will be a tuple.
    # which will not work in the cv.calchist function.
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim(0, 256)


plt.show()
cv.waitKey(0)
