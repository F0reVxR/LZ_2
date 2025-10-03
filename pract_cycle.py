Sum = 0
Numb = (input('Введите целые числа ')).split()
for i in range(0,len(Numb)):
    Numb[i] = int(Numb[i])
print(Numb)
match(int(input('Введите операцию (0 / 1 / 2 / 3) - '))):
    case 0:
        for i in range(0,len(Numb)):
            Numb[i] = 0
        print(Numb)
    case 1:
        for i in range(0,len(Numb)):
            Numb[i] = Numb[i] * 2
        print(Numb)
    case 2:
        for i in range(0,len(Numb),2):
            Numb[i] = Numb[i] + 10
        print(Numb)
    case 3:
        for i in range(0,len(Numb),3):
            if Numb[i] >= 0:
                Numb[i] = float(Numb[i] ** 0.5)
            else:
                Numb[i] = 0
        print(Numb)
    case _:
        for i in range(0,len(Numb)):
            Sum += Numb[i]
        print('Сумма числецов в твой списка: ', Sum)