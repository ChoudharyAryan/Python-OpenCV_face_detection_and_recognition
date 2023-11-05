import cv2 as cv
import numpy as np

img = cv.imread("images/cats/2.jpg")
# cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

blank = np.zeros(
    img.shape, dtype="uint8"
)  # This blank is a list numpy arrays filled with zeros of a given shape and type.
# cv.imshow("blank", blank)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)  # these numerical values are Lower & Upper thresold
cv.imshow("canny", canny)

# ret, thresh = cv.threshold(
#     gray, 125, 255, cv.THRESH_BINARY
# )  # It Looks at an image and tries to binaries that image so if a particular pixil is less than 125 so it will be set to zero or if its above 125 it will be set to max value which in this case is white.
# It will return two outputs first is the thresold that was used and the second is the thresholded image.
# cv.imshow("thresh", thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours are different from edges it is a curve joining continus points [it's a list].
# hierarchies = hierarchiel representation of contours like rectangle --> square --> circle (--> means inside) so this hierarchie is essentialy the representation that open cv uses to find these contours.
# cv.RETER_LIST = it is a MOD in which the method finds and returns the contours.
# cv.Chain_Approx_Simple = it compresses all the contours in the simple one that make more sense(like if you have a have a line than it compresses it to two end points of a line).
print(f"{len(contours)} contours found!")

cv.drawContours(
    blank, contours, -1, (0, 0, 255), 1
)  # Function that draws contours[list] on a image[blank],-1 for all contours,1 for thickness.
cv.imshow("blank image", blank)

cv.waitKey(0)
