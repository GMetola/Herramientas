import numpy as np
import matplotlib.pyplot as plt

mypath = "C:/Users/Gabriel/Documents/Universidad/MOVA_heavy_files/RecognitionStats/"

# no consigo utilizar loadtxt
ground = np.genfromtxt(mypath+'groundtruth.csv',
                    delimiter=",",skip_header=1,
                    dtype = "unicode")
detection = np.genfromtxt(mypath+'detection.csv',
                    delimiter=",",skip_header=1,
                    dtype = "unicode")


# before dividing detection by ground we must exclude non-numerical terms
# this function looks for "-" in column 1 and gives back the indexes
find_errors = np.where(ground[:,1]=="-")[0]

detection[find_errors,:] = 0
ground[find_errors,:] = 0

ground = ground.astype(np.float32)
detection = detection.astype(np.float32)

relation = detection / ground * 100

koi=[]
for column in range(relation.shape[1]):
    for d in range(6):
        k = 50 + 50*d
        koi[d] = np.where(relation[:,column] < k)[0].size

