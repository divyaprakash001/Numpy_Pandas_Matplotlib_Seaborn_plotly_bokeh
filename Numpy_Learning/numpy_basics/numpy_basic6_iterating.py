import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


# iterating or loop
# for i in a1:
#   print(i)

# for i in a2:
#   print(i)
  
# to iterate all elements of any dimension
for i in np.nditer(a3):
  print(i)
  if i == 5:
    print(f"main yaha aya chuka hu {i}")