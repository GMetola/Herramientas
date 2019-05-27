import numpy as np
from PIL import Image, ImageFilter
from random import randint, randrange
import os


def blurring (image):
    return [blurred.append(image.filter(ImageFilter.GaussianBlur(randint(2, 10))))]


def resizing (image):
    final_growth = growth[randrange(0,len(growth))]
    final_size = (int(image.height*final_growth),int(image.width*final_growth))
    return [resized.append(image.resize(final_size))]


def transposing (image):
    # "opciones.get(1)" sería equivalente a "left_to_right" y por eso despues añadimos "(image)",
    #  para darle argumento a la función llamada en el diccionario--> left_to_right(image) for image in pictures
    return [transposed.append(trans_op.get(randint(1, 6),lambda:'Invalid call to dictionary')(image))]


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
growth = np.arange(0.25, 25, 0.25)
transposed = []

trans_op = {
    1: left_to_right,
    2: top_to_bottom,
    3: rotate90,
    4: rotate180,
    5: rotate270,
    6: transpose}

aumen = int(input('¿Cuántas veces quiere repetir la muestra? 5,10 o 20?'))
i = 0
while i < 4:
    if aumen == 5 or aumen == 10 or aumen == 20:
        break
    else:
        aumen = int(input('Lo siento, introduzca una de estas opciones: 5,10 o 20'))
    i += 1
    if i == 3:
        print('Acierte usted')
        exit()

mypath = 'C:/Users/Gabriel/PycharmProjects/prueba/semuere/'
picture_data = os.listdir(mypath)

# abro todas las imágenes en una lista. puedo llamar la las imágenes como quiera
pictures = [Image.open(mypath+cualquier_cosa) for cualquier_cosa in picture_data]

j = 0
eleccion =[]
for p in range(aumen):
    for image in pictures:
        # ELEGIR OPCIÓN DE MODIFICACIÓN
        eleccion.append(randint(1, 3))
        opciones_modificacion.get(eleccion[j], lambda:'Fallo modificación')(image)
        j += 1
print('pictures producidas:', j, '\ncambios:', eleccion)
