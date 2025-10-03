import numpy as np
from datetime import datetime
import time

# array = np.array([1,2,3,4])

# array = array * 3
# print(array)

# print(type(array))
f= ''
t=''
now = datetime.now()
# print(now)
f = now

# array = np.array([[['A','B','C'],['E','F','G']],[['H','I','J'],['H','I','J']]])
array = np.array([
  [['A','B','C'],['E','F','G'],['H','I','J']],
  [['I','J','K'],['L','M','N'],['O','P','Q']],
  [['R','S','T'],['U','V','W'],['X','Y','Z']],
  ])
# print(array)
# print(array.ndim)
# print(array.shape)

# chained indexing
# print(array[0][0][0])

# for i in array:
#   for j in i:
#     for k in j:
#       print(k)

      


# multidimensional indexing

# print(array[1,1,1])


word = array[0,0,0] + array[2,0,0] + array[2,0,0]
# print(word)


array1 = np.array([
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
])

# array1
# array1[start:end:step]


# row selection -----------------

# print(array1[0:4])
# print(array1[0:2])
# print(array1[1:])
# print(array1[:4:2])
# print(array1[::2])
# print(array1[::-2])
# print(array1[1::2])
# print(array1[::2])

# reverse order row selection --------
# print(array1[::-1])
# print(array1[::-2])


# column selection 
# print(array1[:,0])
# print(array1[:,-1])
# print(array1[:,0:2])
# print(array1[:,1::2])
# print(array1[:,::-2])
# print(array1[0:2,0])

# before first comma, its row and then column slicing
# print(array1[0:2,0:2])
# print(array1[0:2,2:4])
# print(array1[2:,:2])
# print(array1[2:,2:])

t = datetime.now() - f
print(t)