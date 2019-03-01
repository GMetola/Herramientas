# FEATURE MATCHING: SIFT AND SURF
import cv2
from matplotlib import pyplot as plt

folder = "C:\\Users\\Gabriel\\Desktop\\"
jorge= cv2.imread(folder + "jorge.jpg", 0)
ezequiel = cv2.imread(folder + "ezequiel.jpg", 0)

orb = cv2.ORB_create()
bfm = cv2.BFMatcher(cv2.NORM_HAMMING)

kp_1, des_1 = orb.detectAndCompute(jorge, None)
kp_2, des_2 = orb.detectAndCompute(ezequiel,None)

matches = bfm.match(des_1, des_2)
matches = sorted(matches, key = lambda x: x.distance)
iguales = cv2.drawMatches(jorge, kp_1, ezequiel, kp_2, matches[:10], None, flags = 2)

plt.imshow(iguales), plt.show()