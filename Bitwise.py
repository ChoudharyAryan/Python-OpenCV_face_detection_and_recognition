import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# Bitwise AND --> Find's the Intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR --> Find's the Intersecting as well as non-intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise Or", bitwise_or)

# Bitwise NOT --> It inverts the binary color.
bitwise_not = cv.bitwise_not(circle)
cv.imshow("Bitwise Not", bitwise_not)

# Bitwise XOR -->Find's the non-intersecting region when the images are over laped.
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOr", bitwise_xor)


cv.waitKey(0)
