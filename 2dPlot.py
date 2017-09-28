import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import pandas as pd
from sys import exit
from mpl_toolkits.mplot3d import Axes3D

ax=plt.figure().gca(projection='3d')
plotGraph = True
run = True
n = 100
space = [[0 for j in range(n)] for i in range(n)] # x , y
alt = [[0 for j in range(n)] for i in range(n)] # z


def update_lines(num, data, line):
    line.set_data(data[0:2, :num])    
    line.set_3d_properties(data[2, :num])    
    return line

def defineRoad(a,b,c,d):
	#print("Defining road")
	plotRoad(a,b,c,d)
	for i in range(a,b+1):
		for j in range(c,d+1):
			space[i][j] = 1
	xx,yy = np.meshgrid(range(a,b+1),range(c,d+1))
	z = 0

	return

def defineBuilding(a,b,c,d,h):
	plotBuilding(a,b,c,d,h)
	for i in range(a,b+1):
		for j in range(c,d+1):
			space[i][j] = h
	return

def plotRoad(a,b,c,d):
	if(plotGraph):
		xx,yy=np.meshgrid(range(a,b),range(c,d))
		z=0
		ax.plot_surface(xx,yy,z,alpha=0.2,color='b')
		return

def plotBuilding(a,b,c,d,h):
	if(plotGraph):
		xx,yy=np.meshgrid(range(a,b),range(c,d))
		ax.plot_surface(xx,yy,0,alpha=0.2,color='r',lw = 2)
		return


def saveCode():
	fl = open("space.txt", "wb")
	df = pd.DataFrame(space)
	fl.write(df.to_csv(index=False, header=False))
	return

#roads
defineRoad(60,70,0,65)
defineRoad(0,99,65,75)

#buildings
defineBuilding(2,12,2,10,45)
defineBuilding(2,12,14,24,50)
defineBuilding(2,12,26,40,50)
defineBuilding(2,12,48,62,60)

defineBuilding(14,24,2,10,45)
defineBuilding(14,24,14,24,50)
defineBuilding(14,24,26,40,50)
defineBuilding(14,24,48,62,60)

defineBuilding(34,50,2,15,45)
defineBuilding(34,50,17,29,50)
defineBuilding(34,50,31,61,50)


defineBuilding(2,12,77,89,45)
defineBuilding(16,30,77,89,50)
defineBuilding(34,50,77,89,50)
defineBuilding(53,70,77,89,50)
defineBuilding(74,94,77,89,50)


defineBuilding(73,82,2,15,30)
defineBuilding(73,82,17,45,60)
defineBuilding(84,97,2,19,70)
defineBuilding(84,97,21,51,45)

arr = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]


for i in range(n):
	for j in range(n):
		if(space[i][j] == 1):
			arr[i][j][0] = 1
		elif(space[i][j] > 1):
			for k in range(space[i][j]):
				arr[i][j][k] = 1
		else:
			arr[i][j][0] = 0


for i in range(n):
	for j in range(n):
		if(space[i][j] > 0):
			print(1,end='')
		else:
			print(" ",end='')
	print()

plt.show()


