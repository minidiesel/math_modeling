import matplotlib.pyplot as plt

def  stairs(N=0, title='лестница'):
    x=[0]
    y=[0]
    
    for i in range(N):
        x+=[i,i+1]
        y+=[i+1]*2
        
    plt.plot(x,y, color='r',label='лестница')
    
    plt.legend()
    plt.title(title)
    
    plt.show()
    
num=int(input('кол-во ступенек: '))
stairs(num)