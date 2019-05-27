import cv2
import time
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--video', required=True, help='path to video file', default=True)
    argumentos = parser.parse_args()


    cap = cv2.VideoCapture(r'F:\Portatil\Vision Artificial\Herramientas\eye_face\avengers.mp4')
    i = 0
    start = time.time()

    while cap.isOpened():

        i += 1

        ret, frame = cap.read()

        # convertion to gray to find rects easyly
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cascade_path = r"F:\Portatil\Vision Artificial\Herramientas\eye_face\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascade_path)
        rects = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30),
                                             flags=cv2.CASCADE_SCALE_IMAGE)

        cascade_path = r"F:\Portatil\Vision Artificial\Herramientas\eye_face\haarcascade_eye.xml"
        eyeCascade = cv2.CascadeClassifier(cascade_path)
        elipses = eyeCascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(5, 5),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
        # apply rects to the colored image
        [cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) for x, y, w, h in rects]
        [cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3) for x, y, w, h in elipses]

        cv2.imshow('detected!', frame)

        # to calculate fps:
        if i % 10 == 0:
            end = time.time()
            fps = i / (end - start)
            print('Current fps: ', int(fps))
            print('Actual time: ', round(end - start, 2), '\n')

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print('Number of frames: ', i)
    print('Average fps: ', i / (end - start))
