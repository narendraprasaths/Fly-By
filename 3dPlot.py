import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import pandas as pd
from sys import exit
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.hold(True)

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


def saveCode():
	fl = open("space.txt", "wb")
	df = pd.DataFrame(space)
	fl.write(df.to_csv(index=False, header=False))
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
		for z in range(h):
			ax.plot_surface(xx,yy,z,alpha=0.09,color='lightblue',lw = 2)

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

"""
defineRoad(60,70,0,65)
defineRoad(0,99,65,75)

#buildings
defineBuilding(2,12,2,10,7)
defineBuilding(2,12,14,24,7)
defineBuilding(2,12,26,40,7)
defineBuilding(2,12,48,62,7)

defineBuilding(14,24,2,10,7)
defineBuilding(14,24,14,24,7)
defineBuilding(14,24,26,40,7)
defineBuilding(14,24,48,62,7)

defineBuilding(34,50,2,15,7)
defineBuilding(34,50,17,29,7)
defineBuilding(34,50,31,61,7)


defineBuilding(2,12,77,89,7)
defineBuilding(16,30,77,89,7)
defineBuilding(34,50,77,89,7)
defineBuilding(53,70,77,89,7)
defineBuilding(74,94,77,89,7)


defineBuilding(73,82,2,15,7)
defineBuilding(73,82,17,45,7)
defineBuilding(84,97,2,19,7)
defineBuilding(84,97,21,51,7)"""

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

def checkCube(x,y,z):
	xRange_min = 0
	xRange_max = 0
	yRange_min = 0
	yRange_max = 0
	zRange_min = 0
	zRange_max = 0
	if(x - 1 > -1):
		xRange_min = x - 1
	if(y - 1 > -1):
		yRange_min = y - 1
	if(z - 1 > -1):
		zRange_min = z -1 

	if(x+2 < 100):
		xRange_max = x + 2
	if(y+2 < 100):
		yRange_max = y + 2
	if(z+2 < 100):
		zRange_max = z + 2
	pass

def generatePath(x1,y1,z1,x2,y2,z2):
	#print("path creation started")
	#print(x1,y1,x2,y2)
	x = x2 - x1
	y = y2 - y1
	xx = []
	yy = []
	#print(x,y)
	if(x > y):
		div = y/x
		#print(div)
		#print(y1,y2)
		n = y1
		while(n > y2):
			yy.append(n)
			n = n + div

		for i in range(len(yy)):
			yy[i] = round(yy[i])

		xx = [x for x in range(x1,x2)]
	elif(y>x):
		div = x/y
		n = x1
		while (n > x2-1):
			xx.append(n)
			n = n + div

		for i in range(len(xx)):
			xx[i] = round(xx[i])

		yy = [x for x in range(y1,y2+1)]
	points = []
	height = []
	#print(len(xx),len(yy))
	for i in range(len(xx)):
		points.append([xx[i],yy[i]])
		height.append(space[xx[i]][yy[i]])
	maxHeight = max(height)+1
	track = []

	track = verticalTakeOff(points,maxHeight,track)
	track = defPath(points,maxHeight,track)
	track = landing(points,maxHeight,track)
	#print(track)
	for i in track:
		#print(i)
		arr[i[0]][i[1]][i[2]] = 1
		space[i[0]][i[1]] = i[2]

	#ax.plot(track[0],track[1],track[2])
	return np.array(track)

def verticalTakeOff(points,height,track):
	initPoint = 0
	for i in range(height):
		track.append([points[0][0],points[0][1],i])
		
	ax.plot([points[0][0],points[0][0]],[points[0][1],points[0][1]],[0,height],color='red')
	return track

def defPath(points,height,track):
	for i in points:
		track.append([i[0],i[1],height])
	initp = points[0]
	finalp = points[len(points)-1]
	ax.plot([initp[0],finalp[0]],[initp[1],finalp[1]],[height,height],color='red')
	return track

def landing(points,height,track):
	finalPoint = finalPoint = points[len(points)-1]
	for i in range(height,0,-1):
		track.append([finalPoint[0],finalPoint[1],i])
	ax.plot([points[0][0],points[0][0]],[points[0][1],points[0][1]],[height,0],color='red')
	return track


	

	
#roads
#data = generatePath(65,15,0,10,70,0)
#data = generatePath(10,70,0,65,15,0)
#data = generatePath(11,71,0,66,16,0)
'''
for k in range(66):
	print(k)
	for i in range(n):
		for j in range(n):
			print(arr[i][j][k],end='')
		print()
	print()
	'''

"""
for i in range(n):
	for j in range(n):
		if(space[i][j] > 0):
			print(space[i][j],end='')
		else:
			print(" ",end='')
	print()"""


if(plotGraph):
	#line = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])[0]

	# Setting the axes properties
	ax.set_xlim3d([0.0, 100.0])
	ax.set_xlabel('X')

	ax.set_ylim3d([0.0, 100.0])
	ax.set_ylabel('Y')
		
	ax.set_zlim3d([0.0, 100.0])
	ax.set_zlabel('Z')

	plt.show()	



