import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1,b=1,c=0, title='график парабола'):
    x=np.arange(-10,10,0.125)
    y=a*(x**2)+b*x+c
    plt.plot(x,y,color='r', label='график парабола')
    plt.xlabel('ось x')
    plt.ylabel('ось y')
    plt.title(title)
    plt.legend()
    plt.show
    
parabola_plotter()



def giperbola_plotter(q=1,title='график гипербола'):
    x_min=-20
    x_max=20
    x=np.arange(x_min,x_max, 0.125)
    y=q/x
    y=np.ma.masked_less(y, x_min)
    y=np.ma.masked_greater(y, x_max)
    plt.plot(x,y,color='b', label='график гипербола')
    plt.xlabel('ось x')
    plt.ylabel('ось y')
    plt.title(title)
    plt.legend()
    plt.show
    
giperbola_plotter()

