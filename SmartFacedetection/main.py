import cv2
import os

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


def detect_face_and_save_screenshot(frame, train_data, mouse_dragged):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_points = train_data.detectMultiScale(gray_frame)
    for (x, y, w, h) in face_points:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (5, 71, 240), 4)
        face = frame[y:y + h, x:x + w]
        if mouse_dragged:
            take_screenshot(face, 'screenshot.png')


train_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

mouse_dragged = False


def on_mouse(event, x, y, flags, params):
    global mouse_dragged
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_dragged = True
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_dragged = False


cv2.namedWindow('Window')
cv2.setMouseCallback('Window', on_mouse)

while True:
    successful_frame_read, frame = webcam.read()
    detect_face_and_save_screenshot(frame, train_data, mouse_dragged)
<<<<<<< HEAD
    cv2.imshow('Window', frame)
    key = cv2.waitKey(1)
=======
    cv2.imshow('Window', frame)    key = cv2.waitKey(1)
>>>>>>> 8c37cc3 (Initial commit)
    if key == 81 or key == 113 or key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
