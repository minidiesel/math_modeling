import matplotlib.pyplot as plt
import numpy as np

def xy(r,phi):
     return r*np.cos(phi), r*np.sin(phi)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')  

phis=np.arange(0,6.28,0.01)
r =1.
ax.plot( *xy(r,phis), c='r',ls='-' )
plt.show()



import numpy as np
from matplotlib import pyplot as plt
from math import pi

u=1.     #x-position of the center
v=0.5    #y-position of the center
a=2.     #radius on the x-axis
b=1.5    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')#разметка(сеточка)
plt.show()