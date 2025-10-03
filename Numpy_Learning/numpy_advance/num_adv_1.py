

# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c= []
# import time

# start = time.time()

# for i in range(len(a)):
#   c.append(a[i] + b[i])

# pinter = (time.time() - start)
# print(pinter)

# import numpy as np

# a = np.arange(10000000)
# b = np.arange(10000000,20000000)


# import time

# start = time.time()

# c = a+b

# inter = (time.time() - start)
# print(inter)

# # how much larger time it takes then numpy
# print(pinter / inter)


# -------------------------------------------------------

# let's calculate the size taken between list or numpy array

a = [i for i in range(10000000)]
import sys
size = sys.getsizeof(a)
print(size)


# ----------------
import numpy as np

a = np.arange(10000000)
# a = np.arange(10000000,dtype=np.int32)
# a = np.arange(10000000,dtype=np.int16)
# a = np.arange(10000000,dtype=np.int8)
import sys
size = sys.getsizeof(a)
print(size)