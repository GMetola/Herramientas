import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([2,2,2])
c=np.array([8,8,8])

print(a)

j=0
comparing=[]
for j in range(np.size(a,0)):
    comparing.append(np.greater(a[j,:],b))

j=0
disparing = []
for j in range(np.size(a,0)):
    disparing.append(np.less(a[j,:],c))

print(comparing)
print(disparing)
prueba=[]
j=0
for j in range(len(a)):
    prueba.append(comparing [j] * disparing[j])

print(prueba)

hello_wor(parth)