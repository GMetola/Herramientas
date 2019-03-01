import cv2

mypath = "C:/Users/Gabriel/Desktop/"
image = cv2.imread(mypath + "DSC_1012.jpg")

cascade_path = r"C:\Users\Gabriel\Documents\Universidad\MOVA_heavy_files\Eye_face\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascade_path)
rects = faceCascade.detectMultiScale(image,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(10, 10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)

[cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3) for x,y,w,h in rects]

cv2.namedWindow("ventana",flags=cv2.WINDOW_NORMAL)
cv2.imshow('ventana',image)
cv2.waitKey(0)
cv2.destroyAllWindows()