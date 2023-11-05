import cv2 as cv

# Face detection in images--------------------------------------------------

# img = cv.imread("images/humans/7.jpg")
# cv.imshow("human_face", img)

# blurr = cv.GaussianBlur(img,(7,7),0)

# Now face detection Harr Cascades does not involve skin tone or the colors that are present in the image. These Harr cascades essentialy look at an object and in an image and using the edges tries to determine weather it's is a face or not.
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)# if you give blurr in place of img then it wont recognize her stomach as face just in this specific image.
# cv.imshow("gray", gray)

harr_cascade = cv.CascadeClassifier(
    "Harr_face.xml"
)  # Reads those thousands of lines and stores them in the variable
# faces_rect = harr_cascade.detectMultiScale(
#     gray, scaleFactor=1.1, minNeighbors=1
# )  # what it does is the instance of CascadeClassifiers takes in the grayscale image and use these variables called solefactor and minneghibour to essentially detect a face and return a rectungular coordinates of that face as a list to faces_rect.

# print(f"Number of faces found ={len(faces_rect)}")

# for x, y, w, h in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# cv.imshow("human_face_detected", img)

# Face detection in videos-----------------------------------------------

# capcture = cv.VideoCapture("videos/8.mp4")

# while True:
#     isTrue, frame = capcture.read()
#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     frame_rect = harr_cascade.detectMultiScale(
#         frame_gray, scaleFactor=1.1, minNeighbors=3
#     )
#     print(f"Number of faces found ={len(frame_rect)}")
#     for x, y, w, h in frame_rect:
#         cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

#     cv.imshow("video", frame)

#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break

# capcture.release()
# cv.destroyAllWindows()


# Face detection in webcam----------------------------------------------

capcture = cv.VideoCapture(0)

while True:
    isTrue, frame = capcture.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_rect = harr_cascade.detectMultiScale(
        frame_gray, scaleFactor=1.1, minNeighbors=3
    )
    print(f"Number of faces found ={len(frame_rect)}")
    for x, y, w, h in frame_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capcture.release()
cv.destroyAllWindows()


# cv.waitKey(0)
