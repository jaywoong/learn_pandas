import pandas as pd;
import numpy as np;

df1 = pd.DataFrame(
    {
        '상품번호':['p1','P1','p2','P2'],
        '수량':   ['3,000','2,000','5,000','6,000']
    }
);
print(df1);
df1['상품번호'] = df1['상품번호'].str.upper()
df1['수량'] = df1['수량'].str.replace(',','')
df1 = df1.astype({'수량':float})
print(df1)

gdf1 = df1.groupby(by=['상품번호'], as_index=False).count()
print(gdf1)

t = pd.read_csv('test.csv')
print(t.shape)
print(t.columns)
t1 = t.groupby(by = ['pclass','sex'], as_index=False).count()
print(t1)
t1 = t.groupby(by = ['pclass','sex'], as_index=True).mean()['age']
print(t1)