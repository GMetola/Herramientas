import shutil
from os import listdir, path, makedirs
from PIL import Image
import numpy as np


def ColorRange(file_path, image):
    origina_frames = Image.open(file_path)
    hsv_frames = origina_frames.convert('HSV')

    hsv_matrix = np.array(hsv_frames)  # matrix 1024x1280x3 en HSV.

    # range of colors of the object
    low_colors = np.array([29, 43, 126])
    high_colors = np.array([126, 255, 255])

    # comparo is a matrix of (pixels x pixels x 3)
    # that "3" is for H,S,V
    # For Example: it will contain False,True,True if H is out of range and S and V are in range

    comparo = (hsv_matrix > low_colors) & (hsv_matrix < high_colors)
    # rango_lapiz is a (pixels x pixels) matrix, boolean too.
    # I only want the pixels where all H,S AND V are inside the object range
    rango_lapiz = comparo[:, :, 0] * comparo[:, :, 1] * comparo[:, :, 2]

    # it modifies the pixels where the object appears
    hsv_matrix[rango_lapiz] = [255, 255, 255]
    im = (Image.fromarray(hsv_matrix, 'HSV')).convert('RGB')  # el convert aplica a todoo lo de la izquierda

    # returns modified image
    # returns a matrix of pixels with a boolean depending if that pixel belongs to my object
    return im, rango_lapiz

"""
# TODO  
Eliminar pequeños focos de ruido en la imagen resultante: 
i. Aplicar dos operaciones de ​erosión​ consecutivas utilizando un 
elemento estructurante cuadrado de tamaño 3x3. 
ii. Aplicar dos operaciones de ​dilatación​ consecutivas utilizando un 
elemento estructurante cuadrado de tamaño 3x3. 
○ Detectar los distintos contornos que aparecen en la imagen y quedarse 
con aquel que presente mayor área  
○ Presentar en pantalla el resultado del seguimiento: mínimo círculo que 
engloba el objeto detectado en rojo, su centroide en verde y la 
trayectoria del mismo en azul. 

 Por último, se proporciona la secuencia de argumentos que deberá soportar el 
programa presentado. 

python visual_tracking.py --video=./media/lapiz.avi --min_values=29 43 
126 --max_values=88 255 255  
 
"""

ruta = 'C:/Users/Gabriel/PycharmProjects/lapiz-frames/frames/'

# checking the existence of a folder to save the new images
if path.exists(ruta+'nuevas'):
    # if it exists, we delete it
     shutil.rmtree(ruta + 'nuevas')
# we create it anew
makedirs(ruta+'nuevas')

im = []
rango_lapiz = []  # just in case it could be handly
for image in listdir(ruta):  # LISTDIR rocks !!
    if image.endswith(".jpg"):
        [a, b] = ColorRange(ruta + image.__str__(), image)
        im.append(a)
        rango_lapiz.append(b)
        # __str__() includes file extension!!
        file_path = path.join(ruta+'nuevas/'+image.__str__())
        a.save(file_path)
    else:
        continue

# checking:
print('imagenes', len(im))

