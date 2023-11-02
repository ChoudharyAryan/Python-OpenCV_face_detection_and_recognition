import cv2 as cv
import numpy as np


img = cv.imread("images/cats/4.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian Method
# the Laplician method computes the gradient of the grayscale image.
# When we transition from black to white or white to black this is considerd positive or negative slope now image itself can not have a negative pixel value so what we can do is compute the absolute value of that image so all the pixel values of the image are converted to the absolute value and then we convert that to uint8 to an image specific datatype.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplician", lap)

# Sobel
# it computes the gradient in two directions x and y.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobely, sobelx)

cv.imshow("SobelX", sobelx)
cv.imshow("SobelY", sobely)
cv.imshow("Sobel", combined_sobel)


# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)

cv.waitKey(0)
