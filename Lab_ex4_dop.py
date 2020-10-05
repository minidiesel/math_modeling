a = int(input('введите число '))
while a > 1:
    b = 2
    f = 0
    while 1:
        if a%b == 0:
            a = a // b
            print(b, end=' ')
            f = 1
            break
        else:
            b += 1
    if f == 1:
        continue
print()