import cv2 as cv
import numpy as np

# CREATE A DUMMY IMAGE
blank = np.zeros((500, 500, 3), dtype="uint8")  # uint8 is the image datatype
# cv.imshow("blank", blank)

# 1.) Paint the image a certain color
# blank[100:250,300:400] = 255, 0, 0
# cv.imshow("RGB", blank)

# 2.) DRAW A RECTANGLE
cv.rectangle(
    blank, (0, 0), (blank.shape[1] // 2, blank.shape[0]), (0, 0, 255), thickness=-1
)
# cv.imshow("rectangle", blank)

# 3.) DRAW A CIRCLE
cv.circle(
    blank, ((blank.shape[1] // 2, blank.shape[0] // 2)), 150, (255, 0, 0), thickness=-1
)
# cv.imshow("circle", blank)

# 4.) DRAW A LINE
cv.line(
    blank,
    (blank.shape[1] // 2, 0),
    (blank.shape[1] // 2, blank.shape[0]),
    (255, 255, 255),
    thickness=1,
)
# cv.imshow("line", blank)

# 5.) WRITE TEXT ON THE IMAGE
cv.putText(
    blank, "OPEN_CV-PYTHON", (100, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2
)
cv.imshow("Text", blank)

cv.waitKey(0)
