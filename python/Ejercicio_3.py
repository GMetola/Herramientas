import numpy as np
import matplotlib.pyplot as plt


mypath = "F:/Portatil/Vision Artificial/Herramientas/RecognitionStats/"


ground = np.genfromtxt(mypath + 'groundtruth.csv',
                       delimiter=",", skip_header=1,
                       dtype="unicode")
detection = np.genfromtxt(mypath + 'detection.csv',
                          delimiter=",", skip_header=1,
                          dtype="unicode")

find_errors = np.where(ground[:, 1] == "-")[0]
ground[find_errors, :] = 0
detection[find_errors, :] = 0

ground = ground.astype(np.float32)
detection = detection.astype(np.float32)

print("probando")