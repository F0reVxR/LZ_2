N = int(input('Введите N: '))
Z = 0
if N == 0:
        print('Задача выполнена!')
while N != 0:
    Z = Z + 1
    if (N % 3) == 0:
        N = int((N - 10) / 2 )
    elif (N % 2) == 0:
        N = int((N * 3))
    elif (N % 5) == 0:
        N = int((N ** 0.5))
    elif (N % 7) == 0:
        N = int((N ** (1 / 3)))
    else:
        N = int(N - 1)
    if Z == 1_999_999:
        print('Бесконечное количество действий')
        break
if Z < 1_999_999:
    print("Количество операций равно", Z)



      
