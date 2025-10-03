import numpy as np

# a = np.arange(24).reshape(6,4)
# '''[
# [ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  ]'''


# fancy indexing

# want first, third and fourth row
# provide list and in list provide index of row
# print(a[[0,2,3]])

# first, third, fourth and last rows
# print(a[[0,2,3,5]])
# print(a[[0,2,3,-1]])

# first column, second and third column

# print(a[:,[0,2,3]])


# ------------------------------
# boolean indexing

# start, end (exclude), how many numbers
a = np.random.randint(1,100,24).reshape(6,4)
# print(a[a>50])
# print(a[a % 2 != 0])
# print(a[(a>=18) & (a%2==0)])

# find all numbers not divisible by 7

print(a)
print(a[(a%7==0)])
print(a[~(a%7==0)])