import numpy as np


a1= np.random.random((3,3))
# a1 = a1.astype(np.int32)
# a1 = np.round(a1 * 100)
# print(a1)

# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))
# print(np.prod(a1))

# column wise maximum
# axis=0 means column
# print(np.min(a1,axis=0))
# print(np.max(a1,axis=0))
# print(np.prod(a1,axis=0))

# row wise maximum
# axis=1 means row
# print(np.min(a1,axis=1))
# print(np.max(a1,axis=1))
# print(np.prod(a1,axis=1))


# mean/median/std/var

# print(np.mean(a1))
# print(np.mean(a1,axis=0))
# print(np.mean(a1,axis=1))
# print(np.std(a1,axis=1))
# print(np.var(a1,axis=1))

# trigonometry func
# print(np.sin(a1))
# print(np.tan(a1))

# dot product

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
# print(np.dot(a2,a3))


# log and exponents
# print(np.log(a1))
# print(np.exp(a1))

# round floor ceil
n1 = np.random.random((2,3))*100
print(n1)
print(np.round(n1))
print(np.floor(n1))
print(np.ceil(n1))