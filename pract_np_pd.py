import numpy as np 
import pandas as pd
import random as rd

r = {}
for i in range(1,10):
    NA = input('Введите имя: ')
    FN = input('Введите фамилию: ')
    PN = input('Введите отчество: ')
    DT = input('Введите дату рождения: ')
    id = rd.randint(100, 999)
    n = dict[ 'Имя': NA, 'Фамилия': FN, 'Отчество': PN, 'Дата рождения': DT]
    r.update({id:n})
    
print(r)
