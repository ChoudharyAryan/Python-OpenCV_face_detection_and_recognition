import cv2 as cv

img = cv.imread("images/cats/2.jpg")
cv.imshow("cat", img)

# CONVERTING TO GRAY SCALE The gray scale compresses the image to its barest minimum pixel
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# BLUR Removes Edges and Noises from image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# EDGE CASCADE Shows the edges in a image
canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny", canny)

# DILATING adding pixels to boundaries of objects in an image
dilated = cv.dilate(canny, (3, 3), iterations=3)
# cv.imshow("dilated", dilated)

# ERODING disconnecting two points and or removing white noises from image
eroding = cv.erode(dilated, (3, 3), iterations=3)
# cv.imshow("erode", eroding)

# RESIZING
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# CROPING
croped = img[50:200, 200:400]
cv.imshow("croped", croped)

cv.waitKey(0)
