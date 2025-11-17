import numpy as np 
import pandas as pd
import random as rd

r = {}
for i in range(1,3):
    NA = input('Введите имя: ')
    FN = input('Введите фамилию: ')
    PN = input('Введите отчество: ')
    DT = input('Введите дату рождения: ')
    id = rd.randint(100, 999)
    n = { 'Имя': NA, 'Фамилия': FN, 'Отчество': PN, 'Дата рождения': DT}
    r.update({id:n})  
#print(r)

df = pd.DataFrame(r.values(), index=r.keys())
print(df)

df.to_csv('D:/1.csv', encoding = 'utf-8')
df1