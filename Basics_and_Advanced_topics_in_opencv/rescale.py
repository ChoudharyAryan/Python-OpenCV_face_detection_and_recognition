import cv2 as cv


# FUNCTION TO CHANGE RESOLUTION OF LIVE VIDEO FEED ONLY
def changeRes(width, height):
    # WORKS FOR LIVE WEBCAM ONLY
    capture.set(3, width)# 3 stands for width 
    capture.set(4, height)# 4 stands for height
    #capture.set(10, 50)


# RESCALING FUNCTION
# WORKS FOR VIDEOS, IMAGES, LIVE WEBCAM
def rescsaleFrame(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    hieght = int(frame.shape[0] * scale)
    dimensions = (width, hieght)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)# cv.resize function that resizes the image takes in the frame and dimensions.


# READING IMAGES
img = cv.imread("images/cats/1.jpg")
img_resized = rescsaleFrame(img)
# cv.imshow("Pussy", img)
cv.imshow("Pussy", img_resized)

cv.waitKey(0)


# READING VIDEOS
capture = cv.VideoCapture("videos/1.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescsaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):# using d as a key to kill the video while playing.
        break

capture.release()
cv.destroyAllWindows()


# READING VIDEOS FROM webCAM

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    changeRes(500,500);
    cv.imshow("webcam", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
