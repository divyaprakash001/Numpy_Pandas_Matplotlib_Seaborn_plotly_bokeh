import numpy as np

# 1D array or vector
array = np.array([1,2,3,4])
# print(array)


# 2d array or matrix
array_2d = np.array([
  [1,2,3],
  [4,5,6]
])

# print(array_2d)



# 3d array or tensor

array_3d = np.array([
  # include 2 or more 2d array to make 3d
  [[1,2],[3,4]],
  [[5,6],[7,8]],
  [[9,10],[11,12]],
  ]
)

# print(array_3d)
array = np.array([1,2,3,4],dtype=float)
# print(array)

# use
# np.arange
# another way to create numpy array
n2 = (np.arange(1,11))
# print(n2)

# with reshape
n3= (np.arange(1,13).reshape(2,6))
# print(n3)

# create array using this or matric using this ones function
print(np.ones((3,4)))
print(np.ones((3,4),dtype=int))
print(np.zeros((3,4)))
print(np.zeros((3,4),dtype=int))
print(np.random.random((3,4)))

# lower range, upper range, no of items
# in given range it generate points with equal distance
print(np.linspace(-10,10,10))
print(np.linspace(-10,10,10,dtype=int))

# create identity matric
print(np.identity(3))
print(np.identity(3,dtype=int))

