import numpy as np

# a = np.random.randint(1,100,15)
# b = np.random.randint(1,100,24).reshape(6,4)

# sort function -----------------------
# print(np.sort(a))
# print(np.sort(a)[::-1])

# sort for 2D
# sort by column
# print(np.sort(b,axis=0))
# print(np.sort(b,axis=0)[::-1])  #descending order
# sort by rows
# print(np.sort(b,axis=1))


# append function ---------------------- 
# print(np.append(a,200))
# print(np.append(b,np.random.random((b.shape[0],1)),axis=1))
# print(b.shape)

# concatenate function -------------
# c = np.arange(6).reshape(2,3)
# # d = np.arange(6,12).reshape(2,3)
# d = np.array([
#   [6,7,np.nan],[8,np.nan,9]
# ])

# print(c)
# print(d)
# print(np.concatenate((c,d),axis=0))
# print(np.concatenate((c,d),axis=0).shape)
# print(np.concatenate((c,d),axis=1).shape)
# print(np.concatenate((c,d),axis=1))


# unique function
# a = np.array([1,1,2,2,2,3,3,3,5,4,7,3,5,4,6,7,6])
# print(np.unique(a))

# expand_dims ===> expand dimensions
# a = np.random.randint(1,100,15)
# print(a.shape)
# print(np.expand_dims(a,axis=0))
# print(np.expand_dims(a,axis=0).shape)
# print(np.expand_dims(a,axis=1).shape)
# print(np.expand_dims(a,axis=1))


# where
# find all indices with value greater than 50
# a = np.random.randint(1,100,15)
# print(a)
# print(np.where(a>50))

# replace all values > 50 with 0
# condition, if true, if false
# print(np.where(a>50,0,1))
# print(np.where(a>50,0,a))
# print(np.where(a%2==0,0,a))

# argmax == gives index of the max element
# print(a)
# print(np.argmax(a))

# b = np.random.randint(1,100,24).reshape(6,4)
# print(b)
# # print(np.argmax(b))
# # print(np.argmax(b,axis=0))
# # print(np.argmax(b,axis=1))

# print(np.argmin(b,axis=1))
# print(np.argmin(b,axis=0))


# code
# import numpy as np
# a = np.random.randint(1,100,15)
# print(a)
# print(np.cumsum(a))

# print(b)
# print(np.cumsum(b))
# print(np.cumsum(b,axis=0))
# print(np.cumsum(b,axis=1))

# print(a)
# print(np.cumprod(a))
# print(b)
# print(np.cumprod(b))
# print(np.cumprod(b,axis=0))
# print(np.cumprod(b,axis=1))


# a = np.random.randint(1,100,15)
# b = np.random.randint(1,100,24).reshape(6,4)

# print(a)
# print(np.percentile(a,100))
# print(np.percentile(a,0))
# print(np.percentile(a,50))
# import matplotlib.pyplot as plt
# np.histogram
# print(a)
# print(np.histogram(a))
# hist,bin_edges =(np.histogram(a,bins=[0,10,20,30]))
# print(hist)
# print(bin_edges)

# plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge', edgecolor='black')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram (Manual)')
# plt.show()


# a = np.random.randint(1,100,15)
# b = np.random.randint(1,100,24).reshape(6,4)

# salary = np.array([20000,40000,25000,35000,60000])
# experience = np.array([1,3,2,4,2])

# print(np.corrcoef(salary))
# print(np.corrcoef(experience))
# print(np.corrcoef(experience,salary))
# print(np.corrcoef(salary,experience))


# a = np.random.randint(1,100,15)
# items = [10,20,30,40,50,60,70,80,90]
# print(a)
# print(items)
# print(np.isin(a,items))
# print(a[np.isin(a,items)])


# np.flip function
# a = np.random.randint(1,100,15)
# print(a)
# print(np.flip(a))

# b = np.random.randint(1,100,24).reshape(6,4)
# print(b)
# print(np.flip(b,axis=1))
# print(np.flip(b,axis=0))



# np.put function == done permanent changes in array using index position

# a = np.random.randint(1,100,15)
# print(a)
# print(np.put(a,[0,1],[110,530]))
# print(a)

# # np.delete function
# print(np.delete(a,0))
# print(np.delete(a,[0,1]))

# Set functions  ----------------
# np.union1d
# np.intersect1d
# np.setdiff1d
# np.setxor1d
# np.in1d

# a = np.random.randint(1,100,15)
# m = np.array([1,2,3,4,5])
# n = np.array([3,4,5,6,7])

# print(np.union1d(m,n))
# print(np.intersect1d(m,n))
# print(np.setdiff1d(m,n))
# print(np.setxor1d(m,n))
# print(np.isin(m,n))


# np.clip
# numpy.clip() function is used to Clip (limit) the values in an array.

# a = np.random.randint(1,100,15)
# print(a)
# print(np.clip(a,a_min=25,a_max=75))



# a = np.random.randint(1,100,15).reshape(3,5)
# print(a)
# print(np.swapaxes(a,0,1))


# arr = np.arange(8).reshape(2,2,2)
# # Original shape: (2, 2, 2)
# result = np.swapaxes(arr, 0, 2)
# print(arr)
# print(result)
# # New shape: (2, 2, 2) - but axes 0 and 2 swapped

# np.uniform
'''How it works
Returns random floating-point numbers in the interval [low, high).

Every number in the interval has an equal chance of being picked.

Useful for simulations, randomized algorithms, initializing weights in neural networks, and when you need random real numbers in a specific range.'''
# import numpy as np

# # Single value between 0 and 1
# value = np.random.uniform()
# print(value)

# # Five random numbers between 10 and 20
# values = np.random.uniform(low=10, high=20, size=5)
# print(values)

# # 2x3 array of random values between -5 and 5
# arr = np.random.uniform(-5, 5, (2, 3))
# print(arr)



# a = np.random.randint(0,100,15)
# print(a)
# print(np.nonzero(a))

# import numpy as np

# arr = np.array([0, 1, 0, 2, 3])
# print(np.count_nonzero(arr))  # Output: 3 (non-zero: 1, 2, 3)

# arr_2d = np.array([[0, 1, 2], [0, 0, 3]])
# print(np.count_nonzero(arr_2d, axis=0))  # Output: [0 1 2] counts non-zeros column-wise
# print(np.count_nonzero(arr_2d, axis=1))  # Output: [2 1] counts non-zeros row-wise

# bool_arr = np.array([True, False, True])
# print(np.count_nonzero(bool_arr))  # Output: 2 (True counts as 1)


# np.repeat

# a = np.random.randint(0,100,15)
# b = np.random.randint(0,100,15).reshape(3,5)
# # print(np.repeat(a,3))
# print(np.repeat(b,3,axis=0))
# print(np.repeat(b,3,axis=1))

import numpy as np

a = np.array([1.0, 2.0, 3.0])
c = np.array([1.0, 2.0, 3.0])
b = np.array([1.0, 2.00001, 3.0])

print(np.allclose(a, b))      # True (close values)
print(np.array_equal(a, b))   # False (not exactly equal)
print(np.array_equal(a, c))   # True (not exactly equal)
