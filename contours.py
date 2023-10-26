import cv2 as cv

img = cv.imread("images/cats/2.jpg")
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# canny = cv.Canny(blur, 125, 175)  # these numerical values are Lower & Upper thresold
# cv.imshow("canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours are different from edges it is a curve joining continus points [it's a list].
# hierarchies = hierarchiel representation of contours like rectangle --> square --> circle (--> means inside) so this hierarchie is essentialy the representation that open cv uses to find these contours.
# cv.RETER_LIST = it is a MOD in which the method finds and returns the contours.
# cv.Chain_Approx_Simple = it compresses all the contours in the simple one that make more sense(like if you have a have a line than it compresses it to two end points of a line).
print(f"{len(contours)} contours found!")

cv.waitKey(0)
