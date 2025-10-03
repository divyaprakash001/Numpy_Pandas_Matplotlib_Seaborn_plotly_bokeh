import numpy as np
import matplotlib.pyplot as plt

# plotting a 2D plot
x = np.linspace(-10,10,100)
print(x)
# y = x
# y=x**2
# y=np.sin(x)
# y=np.tan(x)
# y =  x * np.log(x)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
plt.show()
