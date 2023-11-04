import cv2 as cv
import numpy as np

harr_cascade = cv.CascadeClassifier("Harr_face.xml")

# features = np.load("features.npy")
# lables = np.load("lables.npy")

people = ["Chrstian_bale", "gal_gadot", "jhony_depp", "tom_hardy", "robert_patinson"]
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(
    "faces/tom_hardy/10268290_ori-e1442346060890-240x240.jpg"
)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect the faces in the image

face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h in face_rect:
    face_roi = gray[y : y + h, x : x + w]

    lable, confidence = face_recognizer.predict(face_roi)
    print(f"Lable =  {people[lable]} with a confidence of {confidence}")

    cv.putText(
        img,
        str(people[lable]),
        (20, 20),
        cv.FONT_HERSHEY_COMPLEX,
        1.0,
        (0, 255, 0),
        thickness=2,
    )
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)


cv.imshow("Person Detected V", img)

cv.waitKey(0)
