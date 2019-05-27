import numpy as np
from PIL import Image,ImageFilter
from random import randint, randrange
import os
import argparse


def blurring (image):
    return image.filter(ImageFilter.GaussianBlur(randint(2, 10)))

def resizing (image):
    growth = np.arange(0.25,25,0.25)
    final_growth = growth[randrange(0,len(growth))]
    final_size = (int(image.height*final_growth),int(image.width*final_growth))
    return image.resize(final_size)

def transposing (image):
    return trans_op.get(randint(1, 6),lambda:'Invalid call to dictionary')(image)

def left_to_right(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def top_to_bottom(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def rotate90(image):
    return image.rotate(90)

def rotate180(image):
    return image.rotate(180)

def rotate270(image):
    return image.rotate(270)

def transpose(image):
    return image.transpose(Image.TRANSPOSE)


opciones_modificacion ={
    1:blurring,
    2:resizing,
    3:transposing}

trans_op = {
    1:left_to_right,
    2:top_to_bottom,
    3:rotate90,
    4:rotate180,
    5:rotate270,
    6:transpose}

ap = argparse.ArgumentParser()
ap.add_argument('-i','--input_dataset', required=True, help = 'Input data path')
ap.add_argument('-f','--factor', required=True, help='number of times the dataset will be augmented')
ap.add_argument('-o','--output_dataset', required=True, help='Output data path')
args = ap.parse_args()

path_in = args.input_dataset
path_out = args.output_dataset
factor = args.factor

# path_in = "./Metola_Fernandez_Gabriel_python/tiny_imagenet/"
# path_out = "./Metola_Fernandez_Gabriel_python/augmented/"
# factor = 5

picture_data = os.listdir (path_in)

if not os.path.exists(path_out):
    os.makedirs(path_out)

j=0
election =[]

for image in picture_data:
    image_name = os.path.join(path_in, image)
    try: 
        picture = Image.open(image_name)
    except Exception as e:
        raise e
        print("Error, that's not an image")
    
    for p in range(int(factor)):
        election.append(randint(1,3))
        modified = opciones_modificacion.get(election[j],lambda:'Modification failure')(picture)
        j+=1        
        try:
            modified.save(os.path.join(path_out, image.split(".")[0] + '_' + str(p+1) +'.jpg'), 'JPEG')
        except:
            print("Error saving image")

print('pictures produced:', j, '\nchanges:', election)

