import numpy as np
from matplotlib import pyplot as plt

data = {'a':(0,2), 'b': (0.2,.3), 'c': (.1,.3), 'd': (0.3,0.4),'e':(.1,.2),'f':(.1,.4)}

width = 0.5 # adjust to your liking

fig, ax = plt.subplots()

for i, values in enumerate(data.values()):

    ymin, ymax = values

    ax.axvspan(xmin=i-width/2, xmax=i+width/2, ymin=ymin,ymax=ymax)

# to illustrate that ranges are properly drawn
ax.grid(True)

#add ticks 
ax.set_xticks(np.arange(0,len(data)))    
ax.set_xticklabels(data.keys())

plt.show()