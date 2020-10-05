a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a<b+c) and (c<a+b) and (b<c+a):
    print('треугольник существует')
    if (a==b) or (c==b) or (a==c):
        print('треугольник равнобедренный')
    elif (a==b==c):
        print('треугольник равносторонний')
    elif (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==b**2+a**2):
        print('треугольник прямоугольный')
    else:
        print('тругольник разносторонний')
else:
    print('треугольник не существует')

