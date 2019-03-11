from random import randint, randrange
import os
import numpy as np
from PIL import Image, ImageFilter


def blurring(imagen):
    return [blurred.append(imagen.filter(ImageFilter.GaussianBlur(randint(2, 10))))]


def resizing(imagen):
    final_growth = growth[randrange(0, len(growth))]
    final_size = (int(imagen.height * final_growth), int(imagen.width * final_growth))
    return [resized.append(imagen.resize(final_size))]


def transposing(imagen):
    # "opciones.get(1)" sería equivalente a "left_to_right" y por eso despues añadimos "(image)",
    #  para darle argumento a la función llamada en el diccionario--> left_to_right(image) for image in pictures
    return [transposed.append(trans_op.get(randint(1, 6), lambda: 'Invalid call to dictionary')(imagen))]

def left_to_right(koi):
    return koi.transpose(Image.FLIP_LEFT_RIGHT)
def top_to_bottom(koi):
    return koi.transpose(Image.FLIP_TOP_BOTTOM)
def rotate90(koi):
    return koi.rotate(90)
def rotate180(koi):
    return koi.rotate(180)
def rotate270(koi):
    return koi.rotate(270)
def transpose(koi):
    return koi.transpose(Image.TRANSPOSE)


opciones_modificacion = {
    1: blurring,
    2: resizing,
    3: transposing}

blurred = []
resized = []
growth = np.arange(0.25, 2.5, 0.25)
transposed = []

trans_op = {
    1: left_to_right,
    2: top_to_bottom,
    3: rotate90,
    4: rotate180,
    5: rotate270,
    6: transpose}

aumen = int(input('Hoy many times would you like to multiply your database? 5, 10 or 20?\n'))
i = 0
while i < 4:
    if aumen == 5 or aumen == 10 or aumen == 20:
        break
    else:
        aumen = int(input("I'am sorry, please insert one of the following: 5, 10 o 20.\n"))
    i += 1
    if i == 3:
        print('You, trolling bastard, lost your chance.')
        exit()

mypath = 'F:/Imágenes/Antiguas/'
#mypath = './tiny-imagenet-200'
picture_data = os.listdir(mypath)

# Abro todas las imágenes en una lista. puedo llamar la las imágenes como quiera
pictures = [Image.open(mypath + cualquier_cosa) for cualquier_cosa in picture_data]

j = 0
eleccion = []
for p in range(aumen):
    for image in pictures:
        # ELEGIR OPCIÓN DE MODIFICACIÓN
        eleccion.append(randint(1, 3))
        opciones_modificacion.get(eleccion[j], lambda: 'Fallo modificación')(image)
        j += 1
print('imágenes generadas: ', j, '\ncambios: ', eleccion)
