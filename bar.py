import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
YSchoolOut = [14.5,14.5,12.5,9.5,17,0,0]
ZWorkOut = [21.5,21.5,21.5,21.5,14,0,21.5]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, YSchoolOut, 0.4, label = 'School')
plt.bar(X_axis + 0.2, ZWorkOut, 0.4, label = 'Work')
  
plt.xticks(X_axis, X)
plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Weekly Schedule")
plt.legend()
plt.show()