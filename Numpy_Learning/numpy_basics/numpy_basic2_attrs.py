import numpy as np


a1=np.arange(10,dtype=np.int32) # 4 bytes
a1=np.arange(10,dtype=np.int64) # 8 bytes
a2=np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
a4 = np.array(["hello"],dtype=str)


# ndim attributes
# print(a1.ndim)
# print(a2.ndim)
# print(a3.ndim)

# shape attributes gives the shape of the array
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)

# size attributes gives the size of the array
# print(a1.size)
# print(a2.size)
# print(a3.size)

# itemsize attributes gives the memory of each item
# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)
# str takes 4bytes for 1 string
# print(a4.itemsize)


# dtype
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)
# print(a4.dtype)

# changing datatype
print(a3.astype(np.int32).itemsize)
a3 = (a3.astype(np.int32))
print(a3.itemsize)
# print(a3.dtype)
# print(a3.itemsize)