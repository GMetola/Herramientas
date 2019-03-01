import numpy as np
from PIL import Image,ImageFilter
from random import randint, randrange
import os
import argparse

def blurring (image):
    return [blurred.append(image.filter(ImageFilter.GaussianBlur(randint(2, 10))))]
def resizing (image):
    final_growth = growth[randrange(0,len(growth))]
    final_size = (int(image.height*final_growth),int(image.width*final_growth))
    return [resized.append(image.resize(final_size))]
def transposing (image):
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

opciones_modificacion ={
    1:blurring,
    2:resizing,
    3:transposing}

blurred = []
resized = []
growth = np.arange(0.25,25,0.25)
transposed = []

trans_op = {
    1:left_to_right,
    2:top_to_bottom,
    3:rotate90,
    4:rotate180,
    5:rotate270,
    6:transpose}

ap = argparse.ArgumentParser()
ap.add_argument('--input_dataset', required=True)
ap.add_argument('--factor', required=True, help='number of times the dataset will be augmented')
ap.add_argument('--output_dataset', required=True)
args = ap.parse_args()

mypath = 'C:/Users/Gabriel/PycharmProjects/prueba/semuere/'
picture_data = os.listdir (args.input_dataset)
pictures = [Image.open(args.input_dataset+cualquier_cosa) for cualquier_cosa in picture_data]

j=0
eleccion =[]
for p in range(args.factor):
    for image in pictures:
        # ELEGIR OPCIÓN DE MODIFICACIÓN
        eleccion.append(randint(1,3))
        opciones_modificacion.get(eleccion[j],lambda:'Fallo modificación')(image)
        j+=1
