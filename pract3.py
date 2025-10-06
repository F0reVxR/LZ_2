import math
n = 0
Numb = (input('Введите целые числа ')).split()
for i in range(0,len(Numb)):
    Numb[i] = int(Numb[i])

match(int(input('Введите операцию (0 / 1 / 2 / 3) - '))):
    case 0:
        minn = min(Numb)
        n = Numb.count(minn)
        print(f'Минимальный элемент: {minn}, Их количество: {n}')  
    case 1:
        maxx = max(Numb)
        n = Numb.count(maxx)
        print(f'Минимальный элемент: {maxx}, Их количество: {n}')
    case 2:
        minn = min(Numb)
        maxx = max(Numb)
        lis = list()
        colvo = maxx - minn
        for i in range(minn, minn + maxx * colvo, maxx):
            lis.append(i)
        print(lis)
        """li = list(range(minn, minn + maxx * colvo, maxx))
        print(li) """
    case 3:
        minn = min(Numb)
        maxx = max(Numb)
        colvo = maxx - minn
        for i in range(minn , minn + maxx * colvo, maxx):
         print(minn ** i) 

        "print(min(Numb))"
        "print(min(Numb))"
        "b = max(Numb) - min(Numb)"
        "for i in range(0,b):"
        "print(c)"
        "c *= max(Numb)"
    case _:
        s = int(sum(Numb)/len(Numb))
        print(s)
        if s >= 0:
         s = math.factorial(s)
        else:
         print(0)
