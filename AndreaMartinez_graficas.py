import numpy as np
import matplotlib as plt
 datos= np.genfromtxt('times_python.csv')
datoscpp= np.genfromtxt('times_cpp.csb')

time=datos[:,0]
n=datos[:,1]
timet=datoscpp= [:,0]
nn= datoscpp =[:,1]

plt.plot (time,n)
plt.xlabel("Datos")
plt.ylabel ("Tiempo")

plt.plot (timet,nn)
plt.xlabel("Datos")
plt.ylabel ("Tiempo")
