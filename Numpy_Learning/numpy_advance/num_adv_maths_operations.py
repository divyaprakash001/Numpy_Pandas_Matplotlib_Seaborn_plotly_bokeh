import numpy as np

# a = np.arange(10)
# print(np.sum(a))
# print(np.sin(a))

# ---------------------
# sigmoid
# def sigmoid(array):
#   return 1/(1+ np.exp(-(array)))

# a = np.arange(10)
# print(sigmoid(a))



# loss function in ml
# mean squared error

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

print(actual)
print(predicted)

def mse(actual,predicted):
  return np.mean((actual-predicted)**2)

print(mse(actual=actual,predicted=predicted))


# more loss function
# binary cross entropy 
# categorical cross entropy 
