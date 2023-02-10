import cv2
import os
import numpy as np


def create_data(img_dir):
    images = []
    labels = []
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            image = cv2.imread(os.path.join(img_dir, filename))
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            images.append(gray_image)
            labels.append(np.array([1, 0]))
    return images, labels


def train_new_classifier(images, labels, classifier_path):
    data = np.array(images)
    labels = np.array(labels)

    model = cv2.CascadeClassifier()
    model.train(data, labels)
    model.save(classifier_path)
    print("New classifier trained and saved at", classifier_path)


img_dir = os.path.join(os.getcwd(), 'screenshots')
images, labels = create_data(img_dir)
classifier_path = os.path.join(os.getcwd(), 'new_classifier.xml')
train_new_classifier(images, labels, classifier_path)
