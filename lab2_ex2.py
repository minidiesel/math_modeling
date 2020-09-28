b1=int(input('первый член:'))
q=int(input('множетелели :'))
n=int(input('кол-во: '))
for i in range(1, n, 1):
    b=b1*q**(i)
    print(b, end=' ')