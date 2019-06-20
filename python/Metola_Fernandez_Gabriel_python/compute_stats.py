import numpy as np
import matplotlib.pyplot as plt
import argparse, collections
import os

ap = argparse.ArgumentParser(description='Measure error')
ap.add_argument('-inf', '--inference', required=True, metavar='', help= 'path of inference')
ap.add_argument('-gt', '--groundtruth', required=True, metavar='', help= 'path of groundtruth')
ap.add_argument('-out','--output_graphs',required=True, metavar='', help='path to save graphs')
args = ap.parse_args()

inference = args.inference
groundtruth = args.groundtruth
output_graphs = args.output_graphs

"""
inference = './detection.csv'
groundtruth ='./groundtruth.csv'
output_graphs = './output_graphs'
"""

if not os.path.exists(output_graphs):
    os.makedirs(output_graphs)
else:
    for file in os.listdir(output_graphs):
        os.remove(output_graphs + '/' + file)

# no consigo utilizar loadtxt
ground = np.genfromtxt(inference,
                    delimiter=",",skip_header=1,
                    dtype = "unicode")
detection = np.genfromtxt(groundtruth,
                    delimiter=",",skip_header=1,
                    dtype = "unicode")


# before dividing detection by ground we must exclude non-numerical terms
# this function looks for "-" in column 1 and gives back the indexes

not_errors = np.where(ground[:,1] != "-")[0]
num_errors = len(np.where(ground[:,1] == "-")[0])
num_values = len(ground)

relation = np.zeros(ground.shape)
for valor in not_errors:
    relation[valor, :] = (np.absolute(detection[valor, :].astype(np.float) - ground[valor, :].astype(np.float))).astype(int)



### Complexity ###

bins = np.array([0, 1, 2, 3, np.max(relation) + 1])
etiquetas = ('Errors', '0', '1', '2', '3', '=>4')
pos_etiquetas = np.arange(len(etiquetas))

Complexity_sort = collections.Counter(np.digitize(relation[:, 3], bins))
Complexity_sort[0] = num_errors
Complexity_sort[1] -= Complexity_sort[0]
# Bars unsupported for type(s) 'Counter' --> we convert to ndarray
Complexity_count = np.zeros(len(Complexity_sort))

for i in np.arange(len(Complexity_sort)):
    Complexity_count[i] = Complexity_sort[i]

# percentage calculation
Complexity_count = Complexity_count * 100 / num_values

# graphic representation
plt.bar(np.arange(len(Complexity_count)), Complexity_count, color=['k', 'r', 'r', 'r', 'r'])
plt.xticks(pos_etiquetas, etiquetas)
plt.yticks(np.arange(0, 120, 20))
plt.xlabel('Difference between detection and ground')
plt.ylabel('Percentage of total measures')
plt.title('Complexity')
plt.ylim([0, 100])
plt.savefig(output_graphs+'/Complexity.png')
# to clear current figure and don't affect the following
plt.gcf().clear()


### AREA 2D ###

bins = np.array([0,50,100,150,200,250,np.max(relation)+1])
etiquetas = ('Errors','0-50','50-100','100-150','150-200','200-250','250+')
pos_etiquetas = np.arange(len(etiquetas))

Area2D_sort = collections.Counter(np.digitize(relation[:, 1], bins))
Area2D_sort[0] = num_errors
Area2D_sort[1] -= Area2D_sort[0]

# Bars unsupported for type(s) 'Counter' --> we convert to ndarray
Area2D_count = np.zeros(len(Area2D_sort))
for i in np.arange(len(Area2D_sort)):
    Area2D_count[i] = Area2D_sort[i]

# percentage calculation
Area2D_count = Area2D_count * 100 / num_values

# graphic representation
plt.xticks(pos_etiquetas, etiquetas)
plt.xlabel('Difference between detection and ground')
plt.ylabel('Percentage of total measures')
plt.title('Area 2D')
plt.bar(np.arange(len(Area2D_count)), Area2D_count, color=['k', 'r', 'r', 'r', 'r', 'r', 'r'])
plt.ylim([0, 100])
plt.savefig(output_graphs+'/Area 2D.png')
# to clear current figure and don't affect the following
plt.gcf().clear()


### AREA 3D ###

# borro datos de la grafica anterior

Area3D_sort = collections.Counter(np.digitize(relation[:, 2], bins))
Area3D_sort[0] = num_errors
Area3D_sort[1] -= Area3D_sort[0]

# Bars unsupported for type(s) 'Counter' --> we convert to ndarray
Area3D_count = np.zeros(len(Area3D_sort))
for i in np.arange(len(Area3D_sort)):
    Area3D_count[i] = Area3D_sort[i]

# percentage calculation
Area3D_count = Area3D_count * 100 / num_values

# graphic representation
plt.xticks(pos_etiquetas, etiquetas)
plt.xlabel('Difference between detection and ground')
plt.ylabel('Percentage of total measures')
plt.title('Area 3D')
plt.bar(np.arange(len(Area3D_count)), Area3D_count, color=['k', 'r', 'r', 'r', 'r', 'r', 'r'])
plt.ylim([0, 100])
plt.savefig(output_graphs+'/Area 3D.png')
# to clear current figure and don't affect the following
plt.gcf().clear()