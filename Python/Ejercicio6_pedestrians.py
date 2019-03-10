import cv2
import os
import numpy as np


if __name__ == '__main__':

    path = 'F:/Portatil/Vision Artificial/Herramientas/pedestrian_sequence/'
    folder = os.listdir(path)
    img_height, img_width, layers = cv2.imread(path+folder[0]).shape
# TODO cambiar por lista de tamaño 1000
    im_collection = []
    i = 0

    for image in folder:
        cap = cv2.imread(path + image)
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        rectangles, weights = hog.detectMultiScale(gray, winStride=(8, 8),
                                                   padding=(32, 32), scale=1.05)
# ToDO reducir el numero de rectangulos. descartar si weights < 1?
        [cv2.rectangle(cap, (x, y), (x + w, y + h), (0, 255, 0), 3) for x, y, w, h in rectangles]
        cv2.imshow('wololo', cap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        im_collection.append(cap)
        i += 1
# todo incluir barra de progreso
        print("Calculating rectangles: ", i * 100 // (len(folder)), "%")

    out = cv2.VideoWriter('pedestrian detected.avi',
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 15, (img_width, img_height))

    for j in range(len(im_collection)):
        print("Creating video: ", j * 100 // len(im_collection), "%")
        out.write(im_collection[j])
    out.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TODO Cosmin der Große's heavenly tips to turn this shitty code into rocket programming


