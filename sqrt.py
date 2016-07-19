import math
x1=input("Enter the coordinate of x")
y1=input ("Enter the coordinate of y")
z1=input ("Enter the coordinate of z")
x2=input ("Enter the coordinate of x")
y2=input ("Enter the coordinate of y")
z2=input ("Enter the coordinate of z")
x=57.2958*x2-57.2958*x1
y=57.2958*y2-57.2958*y1
z=57.2958*z2-57.2958*z1
total=x**2+y**2+z**2
total = abs(total)
dot=(x1*x2)+(y1*y2)+(z1*z2)
cross=(math.sqrt(x1**2+y1**2+z1**2))*(math.sqrt(x2**2+y2**2+z2**2))
angle=dot/cross
theta=math.acos(angle)
degree=theta*180/math.pi
print ("The angle between the distance is ",degree,"degrees")
num=(math.sqrt(total))
print ("The distance travelled is ",num,"inches")
print ("The angle between the distance is ",degree,"degrees")