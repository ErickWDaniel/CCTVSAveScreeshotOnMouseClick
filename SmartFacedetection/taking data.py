import cv2
import os
import numpy as np

def take_screenshot(frame, filename):
    path = os.path.join(os.getcwd(), filename)
    if os.path.exists(path):
        i = 1
        while True:
            new_filename = filename[:-4] + str(i) + '.png'
            new_path = os.path.join(os.getcwd(), new_filename)
            if not os.path.exists(new_path):
                cv2.imwrite(new_path, frame)
                break
            i += 1
    else:
        cv2.imwrite(path, frame)

def detect_face_and_save_screenshot(frame, train_data):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_points = train_data.detectMultiScale(gray_frame)
    for (x, y, w, h) in face_points:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (5, 71, 240), 4)
        face = frame[y:y + h, x:x + w]
        take_screenshot(face, 'screenshot.png')
        return face

def update_train_data(train_data, face_paths):
    faces = []
    labels = []

    for face_path in face_paths:
        face = cv2.imread(face_path)
        gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        faces.append(gray_face)
        labels.append(1)

    faces = np.array(faces)
    labels = np.array(labels)

    train_data.update(faces, labels)

train_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
face_paths = []

while True:
    successful_frame_read, frame = webcam.read()
    face = detect_face_and_save_screenshot(frame, train_data)
    if face is not None:
        face_paths.append('screenshot.png')
    cv2.imshow('', frame)
    key = cv2.waitKey(1)
    if key == ord('u'):
        update_train_data(train_data, face_paths)
        face_paths = []
    elif key == 81 or key == 113 or key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
