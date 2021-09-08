import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

x2= np.array(["A", "B", "C", "D"])
y2= np.array([2, 4, 0, 4])

plt.bar(x,y)
plt.bar(x2,y2)
plt.show()
