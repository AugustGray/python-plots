import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, 'o:b')

plt.title("Labels Test")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()
