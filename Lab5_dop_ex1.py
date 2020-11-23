from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp, acos
from math import degrees

N=CoordSys3D('N')

#a=4*N.i
#b=4*N.j

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

 # b^c
 
f=a.dot(b)
g=a.dot(c)
h=b.dot(c)
 
a1=a.magnitude()
b1=b.magnitude()
c1=c.magnitude()
 
z=f/(a1*b1)
z1=acos(z)

v=g/(a1*c1)
v1=acos(v)

m=h/(b1*c1)
m1=acos(m)

print(degrees(z1.evalf()))
print(degrees(v1.evalf()))
print(degrees(m1.evalf()))