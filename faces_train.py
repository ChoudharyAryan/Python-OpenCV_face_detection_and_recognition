import os  # The os module in python provides function for interacting with the operating system. the os and os.path modules include many functions to itntrect with the file system.
import cv2 as cv
import numpy as np

people = ["Chrstian_bale", "gal_gadot", "jhony_depp", "tom_hardy", "robert_patinson"]
Dir = r"/home/aryan/Desktop/opencv/faces"
harr_cascade = cv.CascadeClassifier("Harr_face.xml")

features = []
lables = [] # Lable is the index of that particular string in the people list.


def create_train():  # This function will loop over every folder in our base folder and over every image and grab the face from that image and add it to our dataset.
    for person in people:
        path = os.path.join(
            Dir, person
        )  # this join funtion is used to join two paths (path,*path) the *path is the path to be joined.
        lable = people.index(person)

        for img in os.listdir(
            path
        ):  # It is uesd to get the list of all files and directories in the specified deirectory.If not specified than it returns all the files and directories in the current working dierctory.
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray_scale = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = harr_cascade.detectMultiScale(
                gray_scale, scaleFactor=1.1, minNeighbors=10
            )

            for x, y, w, h in faces_rect:
                faces_roi = gray_scale[y : y + h, x : x + w]
                features.append(faces_roi)
                lables.append(lable)


create_train()

features = np.array(features, dtype="object")
lables = np.array(lables)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and lables list
face_recognizer.train(features, lables)
print("Training Done ------------------------")

face_recognizer.save(
    "face_trained.yml"
)  # Now if we want to use this model in another  file we have to do it all over again .So what opencv allow us to do is essentialy save this traind model so that we can use it in another file or another directory or in another world  just by using that particular YAMAL source file .
np.save("features.npy", features)
np.save("lables.npy", lables)  # saves an array to a binary file in Numpy .npy format
