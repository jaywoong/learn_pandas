import pandas as pd
import numpy as np

data = {
    'name':['james1','james2','james3','james4','james5'],
    'ko':[100,90,89,99,89],
    'en':[99,91,87,89,81],
    'ma':[80,92,88,99,87],
    'si':[99,100,87,93,86],
};

df = pd.DataFrame(data)
print(df)

df.index = df['name']
print(df)

del df['name']
print(df)

print(df.loc['james3'],'score')
print(df[df['ko'] > 90])
print(df.loc[df['ko'] > 90, 'en'])
print(df.loc['james4', ['ma', 'si']])

df2 = df.copy()
df2.loc[df['en'] < 90, 'en'] = 90
print(df2)