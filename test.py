import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

xx,yy=np.meshgrid(range(40,60),range(30,40))


plt3d=plt.figure().gca(projection='3d')
for z in range(0,25): 
	plt3d.plot_surface(xx,yy,z,alpha=0.2,color='r')
plt.show()