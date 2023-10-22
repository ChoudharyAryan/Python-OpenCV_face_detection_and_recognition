import cv2 as cv

# READING IMAGES
img = cv.imread("images/cats/9.jpg")

cv.imshow("cat", img)
cv.waitKey(0)

# READING VIDEOS
capture = cv.VideoCapture("videos/1.mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()


# READING VIDEOS FROM webCAM

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    cv.imshow("webcam", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
