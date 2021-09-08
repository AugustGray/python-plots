import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
YSchoolIn = [8,10.5,10.5,8,15,0,0]
YSchoolOut = [14,14.5,12.5,9.5,17,0,0]
ZWorkIn = [15,16,16,12,6.5,0,12]
ZWorkOut = [21.5,21.5,21.5,21.5,14,0,21.5]
  
X_axis = np.arange(len(X))
  

plt.bar(X_axis - 0.2, YSchoolOut, 0.4, label = 'School', color = "#50FA7B")
plt.bar(X_axis - 0.2, YSchoolIn, 0.4, label = 'School', color = "white")
plt.bar(X_axis + 0.2, ZWorkOut, 0.4, label = 'Work', color = "#BD93F9")
plt.bar(X_axis + 0.2, ZWorkIn, 0.4, label = 'Work', color = "white")
  
plt.xticks(X_axis, X)

# plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Weekly Schedule")
plt.legend()
plt.grid()
plt.show()