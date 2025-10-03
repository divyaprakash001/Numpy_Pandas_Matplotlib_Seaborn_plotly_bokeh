import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


# indexing
# ------------------------------
# print(a1)
# print(a1[-1])

# print(a2)
# # row , column to find specific element
# print(a2[1,2])
# print(a2[2,3])
# print(a2[1,0])

# print(a3)
# in which 2d it exist,row,column
# print(a3[1,0,1])
# print(a3[0,1,0])
# print(a3[0,0,0])


# slicing for 1d
# print(a1)
# print(a1[2:5])

# slicing for 2d

# print(a2)
# row, column
# [row:index_slice, which column:index_slice]
# print(a2[0,:])
# print(a2[:,2])

# we want [[5,6],[9,10]]
# print(a2[1:3,1:3])
# print(a2[1:,1:3])

# we want [[0,3],[8,11]]
# [which row:slice:step, which column:slice:step]
# print(a2[::2,::3])

# we want [[1,3],[9,11]]
# print(a2[::2,1::2])

# we want [[4,7]]
# print(a2[1,::3])

# we want [[1,2,3],
#          [5,6,7]]
# print(a2[0:2,1:4])



# slicing for 3d array
# -------------------------

a3 = np.arange(27).reshape(3,3,3)
# print(a3)
'''
  [[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''
# print(a3[1])
# print(a3[::2]) #[[ [ 0  1  2] [ 3  4  5] [ 6  7  8]] [18 19 20] [21 22 23] [24 25 26] ]]
# print(a3[0,1,:]) #[3 4 5]
# print(a3[1,:,1]) #[10 13 16]
# print(a3[2,1:,1:]) # [[22 23] [25 26]]
# we want [[0,2],[18,20]]
# print(a3[::2,0,::2]) # [[0 2] [18 20]]