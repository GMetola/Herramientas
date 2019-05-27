def ColorRange(ruta,image):
    from PIL import Image
    import numpy as np

    origina_frames = Image.open(ruta + '\\' + image.__str__())
    hsv_frames = origina_frames.convert('HSV')

    hsv_matrix = np.array(hsv_frames)  # matrix 1024x1280x3 en HSV.

    # range of colors of the object
    low_colors = np.array([29, 43, 126])
    high_colors = np.array([126, 255, 255])

    # comparo is a matrix of (pixels x pixels x 3)
    # that "3" is for H,S,V
    # it will contain False,True,True if H is out of range and S and V are in range


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

import shutil
from os import listdir,path,makedirs

ruta = r'C:\Users\Gabriel\PycharmProjects\lapiz-frames\all_frames'

# checking the existence of a folder to save the new images
if path.exists(ruta+r'\nuevas'):
    # if it exists, we delete it
     shutil.rmtree(ruta + r'\nuevas')
# we create it anew
makedirs(ruta+r'\nuevas')

im = []
rango_lapiz = []  # just in case it could be handly
for image in listdir(ruta):  # LISTDIR rocks !!
    [a, b] = ColorRange(ruta,image)
    im.append(a)
    rango_lapiz.append(b)
    file_path = path.join(ruta+r'\nuevas',image.__str__())
    # __str__() includes file extension!!
    a.save(file_path)

# checking:
print('  imagenes', len(im), '\n', 'rango_lapiz', len(rango_lapiz))



"""


# pincel=[]
# for row in range(np.size(rgb_matrix,0)):
#    for column in range(np.size(rgb_matrix,1)):
#        if rgb_matrix [row][column][0] < 88:
#            pincel.append(rgb_matrix [row][column] - low_colors)

# print('hsv_matrix',hsv_matrix.shape)
# print('pincel',pincel.shape)
# print(np.size(pincel))
# print(hsv_matrix[1023][1279])
# print(rgb_matrix[1023][1279])


for row in hsv_array:
    pixeles = row
    for element in row:
        lista_hsv = element
        for cono in element:
            lista_cono = cono
            i+=1


print('i',i)
print(pixeles)
print('pixeles',lista_cono.shape)
print('lista_hsv',lista_hsv.shape)
print('hsv_array',len(hsv_array))
prueba = lista_hsv[:,[0]]
pelota_h = np.where(29<prueba)


try:
    hsv_array.append(np.array(hsv_frames[0]))
except: (len(hsv_array)>1030)
h,s,v = hsv_array[0].split
i+=1
# print(hsv_array[0])


# seleccion = np.

# Utilizar colorsys ?????


# [image.show() for image in hsv_frames]

####    pencil= [np.where(np.logical_and(hsv_colors[0]>=29, hsv_frames[0]<88))]
"""