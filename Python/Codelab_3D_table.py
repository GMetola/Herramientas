import numpy as np
import matplotlib.pyplot as plt
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-rg', '--rutaG', required=True, help='ruta de groundtruth')
# args = vars(parser.parse_args())


mypath = "F:/Portatil/Vision Artificial/Herramientas/RecognitionStats/"


# no consigo utilizar loadtxt
ground = np.genfromtxt(mypath + 'groundtruth.csv',
                       delimiter=",", skip_header=1,
                       dtype="unicode")
detection = np.genfromtxt(mypath + 'detection.csv',
                          delimiter=",", skip_header=1,
                          dtype="unicode")

# before dividing detection by ground we must exclude non-numerical terms
# this function looks for "-" in column 1 and gives back the indexes

find_errors = np.where(ground[:, 1] == "-")[0]

print(find_errors.shape)
asdfjasdjklfhasklñdfjñaskld = asklñdfjañklsdfjkl;
cvvvv2.asñdlfuasio. = aiouqwerñkjasdñklfj

print(wolowloooooo)
# NO ES SOLUCIÓN SUSTITUIRLO POR CEROS PORQUE AFECTA A LA GRÁFICA, CAMBIAR!!
# sustituir por NaN ??
# detection[find_errors,:] = 0
# ground[find_errors,:] = 0

"""
ground = ground.astype(np.float32)
detection = detection.astype(np.float32)

relation = detection / ground * 100

koi=[]
for column in np.arange(1,relation.shape[1]):
    for d in range(6):
        k = 50 + 50*d
        koi[d] = np.where(np.asarray(relation[:,column]) < k)[0].size

"""
