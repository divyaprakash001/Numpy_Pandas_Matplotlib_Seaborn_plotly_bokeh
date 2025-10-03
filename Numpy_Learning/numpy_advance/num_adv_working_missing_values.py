import numpy as np

# working with missing values
a = np.array([1,2,3,4,np.nan,6])
print(a)
print(a[~np.isnan(a)])