import cv2
import os
import numpy as np


if __name__ == '__main__':

    path = 'F:/Portatil/Vision Artificial/Herramientas/pedestrian_sequence/'
    folder = os.listdir(path)
    img_height, img_width, layers = cv2.imread(path+folder[0]).shape
    im_collection = np.zeros((img_height, img_width, len(folder)))
    i = 0

    while i != len(folder):
        for image in folder:
            cap = cv2.imread(path + image)
            gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

            rectangles, weights = hog.detectMultiScale(gray, winStride=(8, 8),
                                                       padding=(32, 32), scale=1.05)
### reducir el numero de rectangulos. descartar si weights < 1?
            [cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 5) for x, y, w, h in rectangles]
            im_collection[:, :, i] = gray
            i += 1
            print("Calculating rectangles: ", i * 100 // (len(folder)), "%")

    out = cv2.VideoWriter('pedestrian detected.avi',
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 15, (img_width, img_height))

    for j in range(im_collection.shape[2]):
        print("Creating video: ", j * 100 // im_collection.shape[2], "%")
        out.write(im_collection[j])
    out.release()



