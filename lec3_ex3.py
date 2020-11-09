import lab3_ex1 as lab
import numpy as np
a=100
t=int(input('введите время '))
x0=int(input('введите начальную координату "x" '))
y0=int(input('введите начальную координату "y" '))
v0=int(input('введите начальную скорость '))
if not ((t<=5) and (t>=0)):
    print('введите другое время')
my_array_t=np.zeros(a)
my_array_x=np.zeros(a)
my_array_y=np.zeros(a)

idx=0
for t0 in np.linspace(0, t, a):
    my_array_t[idx]=t0
    my_array_x[idx]=x0+v0*t0
    my_array_y[idx]=y0+v0*t0-(lab.g*t0**2)/2
    idx+=1

rslt= np.stack(( my_array_t, my_array_x, my_array_y), axis=1)
print(rslt)

import matplotlib.pyplot as plt
plt.plot(rslt[:,0], rslt[:,2])
plt.show()