import numpy as np
n = 5
my_array=np.zeros(n)
for i in range(n-1):
    my_array[i] = int(input())
print(my_array)
num = int(input("Число: "))
j = int(input("Позиция: "))
if j>=n:
    print('плохая позиция')
my_array = np.insert(my_array, j, num)
my_array=np.resize(my_array, 5)
np.set_printoptions(suppress=True)
print(my_array)