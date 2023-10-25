import cv2 as cv
import numpy as np

img = cv.imread("images/cats/2.jpg")
cv.imshow("cat", img)


# TRANSLATIONS
def translate(
    img, x, y
):  # x & y are the number of pixels by which we have to shift the image
    transMat = np.float32(
        [[1, 0, x], [0, 1, y]]
    )  # it is a translation matix of type float essentialy 2 by 3  matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(
        img, transMat, dimensions
    )  # this is the function which performs the translation


# -x --> left shift
# x --> right shift
# -y --> up wards
# y --> down wards

translated = translate(img, 100, 100)
#cv.imshow("translated", translated)


# ROTATING THE IMAGE
def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 180)
#cv.imshow("rotated", rotated)


# FLIPPING THE IMAGE
fliped = cv.flip(img, -1)
cv.imshow("fliped", fliped)


cv.waitKey(0)
