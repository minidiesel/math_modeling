a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
D=b**2-4*a*c
if D<0:
    print('нет действительных корней')
if D>0:
    x1=(-b-D**(1/2))/(2*a)
    x2=(-b+D**(1/2))/(2*a)
    print('x1=',x1)
    print('x2=',x2)
if D==0:
    x3=-b/2*A
    print('x=',x3)
    