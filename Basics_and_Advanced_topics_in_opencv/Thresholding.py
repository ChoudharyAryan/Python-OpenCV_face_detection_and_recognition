import cv2 as cv

img = cv.imread("images/cats/2.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 125, 200, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

threshold, thresh_inv = cv.threshold(gray, 125, 200, cv.THRESH_BINARY_INV)
cv.imshow("thresh_inv", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1
)  # cv.ADAPTIVE_THRESH_MEAN_C this is the method of how should the machine calculate the optimal thresold value.THe block is the size of neghiourhood kernel that open cv uses to calculate the mean for optimal threshold value. Now the C value is the integer value subtracted from the mean to fine tune the our threshold.
# on using adaptive_thresholding_Gaussian now it added some weight to pixels.
cv.imshow("adaptive_thresh", adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 10
)
cv.imshow("adaptive_thresh_inv", adaptive_thresh)

cv.waitKey(0)
