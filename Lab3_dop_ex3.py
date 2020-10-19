import numpy as np

a=int(input('количество строк '))
b=int(input('количество столбцов '))
my_array1 = np.zeros(shape=(a,  b))

my_array3=np.zeros(b)
for (i, j), x in np.ndenumerate(my_array1):
     print(i, j, x, sep=';')
     m=input(f'введите значение: [{i},{j}]: ')
     my_array1[i, j]=float(m)
print(my_array1)


for (i, j), x in np.ndenumerate(my_array1):
    if my_array3[j]<my_array1[i, j]:
        my_array3[j]=my_array1[i, j]
print(my_array3)
    
