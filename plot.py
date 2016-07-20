import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

dictFinal={}
values =[]
value1 = {"x":1,"y":2,"z":3}
values.append(value1)
value2 = {"x":10,"y":12,"z":13}
values.append(value2)
values3 = {"x":50,"y":52,"z":63}
values.append(values3)
values4 = {"x":45,"y":42,"z":32}
values.append(values4)
dictFinal["allValues"] = values

print dictFinal
print dictFinal["allValues"][0]['x']
n=len(dictFinal)
print n
print dictFinal["allValues"]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in dictFinal["allValues"]:
	 xs = i['x']
	 ys = i['y']
	 zs =i['z']
	 ax.scatter(xs, ys, zs, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
