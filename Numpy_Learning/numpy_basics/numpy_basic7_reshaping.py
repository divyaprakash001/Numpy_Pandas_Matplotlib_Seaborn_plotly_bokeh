import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


# transpose
print(a2.shape)
print(np.transpose(a2).shape)
print(a2.T)


# ravel => convert any dimension into 1d array
print(a2.ravel())
print(a3.ravel())