import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
YSchoolIn = [8,10.5,10.5,8,15,0,0]
YSchoolOut = [14,14.5,12.5,9.5,17,0,0]
ZWorkIn = [15,16,16,12,6.5,0,12]
ZWorkOut = [21.5,21.5,21.5,21.5,14,0,21.5]
ZWorkMIn = [0, 0, 0, 0, 6.5, 0, 0]
ZWorkMOut = [0, 0, 0, 0, 14, 0, 0]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis, ZWorkOut, 0.4, label = 'Work', color = "#BD93F97F", edgecolor = "#BD93F9", linewidth = '2')
plt.bar(X_axis, ZWorkIn, 0.4, label = 'Work', color = "white", edgecolor = "white", linewidth = '3')
plt.bar(X_axis, YSchoolOut, 0.4, label = 'School', color = "#50FA7B7F", edgecolor = "#50FA7B", linewidth = '2')
plt.bar(X_axis, YSchoolIn, 0.4, label = 'School', color = "white", edgecolor = "white", linewidth = '3')
plt.bar(X_axis, ZWorkMOut, 0.4, color = "#BD93F97F", edgecolor = "#BD93F9", linewidth = '2')
plt.bar(X_axis, ZWorkMIn, 0.4, color = "white", edgecolor = "white", linewidth = '3')
  
plt.xticks(X_axis, X)

plt.ylim(6)

# plt.xlabel("Days")
# plt.ylabel("Hours")
plt.title("Weekly Schedule")
plt.legend()
plt.grid()
plt.show()