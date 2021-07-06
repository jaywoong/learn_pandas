import pandas as pd;
import numpy as np;

data1 = ['A',2];
data2 = ['B',4];

df1 = pd.DataFrame([data1,data2]);
print(df1);

data = {'subject' : ['math', 'comp', 'phys', 'chem'],
        'score': [100, 90, 85, 95],
        'students': [94, 32, 83, 17]};
df2 = pd.DataFrame(data);
print(df2);
print(len(df2));
print(df2.shape);
print(df2.shape[0]);  # 행 정보
print(df2.shape[1]);  # 열 정보

df3 = pd.DataFrame(df2, columns=['students','score','subject']);
print(df3);
print(df3['students'][2]);
print(df3[df3['score'] > 90]);

dic1 = {'math':{1:80,2:90,3:100},'comp':{1:90,2:100}};
df4 = pd.DataFrame(dic1);
print(df4);
