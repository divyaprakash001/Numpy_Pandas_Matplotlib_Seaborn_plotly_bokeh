import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


# horizontal stacking 
# --------------
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

hstack_array = (np.hstack((a4,a5)))
# print(hstack_array)


# vertical stacking 
# --------------
vstack_array = (np.vstack((a4,a5)))
# print(vstack_array)


# splitting
# hsplit like vertical cut
# hsplit_array = np.hsplit(a4,2)
# print(a4)
# print(hsplit_array)

# vsplit like horizontal cut
vsplit_array = np.vsplit(a4,3)
print(a4)
print(vsplit_array)