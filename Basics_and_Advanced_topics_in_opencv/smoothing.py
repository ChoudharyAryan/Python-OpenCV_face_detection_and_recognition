import cv2 as cv

# READING IMAGES
img = cv.imread("images/cats/2.jpg")
cv.imshow("cat", img)

# Averaging
average = cv.blur(img, (3, 3))
# cv.blur does the average bluring .what algorithm did in the background is that it defined a kernel of 3*3 and it computed the center value for a pixel using the average of all sorrounding pixel intensities.
cv.imshow("average", average)

# Gausian Blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
# It does the same thing as Average blur except that insted of computing average of all pixel intensity each sorrounding pixel is given a weight and essentialy the average of the products of those weights gives the value for the center.
# We get less bluring more natural than averaging.
cv.imshow("gausiaan", gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("median", median)
# It is the same as average bluring except it does not find average what it finds is Median of sorrounding pixels.
# Tends to be more effective than both average and Gaussian Blur.


# Bilateral Bluring
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# An even better bluring technique does not use kernel insted uses diameter, sigmacolor is no. of neghibouring colors will be considerd when blur is computed,
# space sigama as in if you give large value means that pixels further out from the central pixel will effect the bluring calcualtion.
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
