import pandas as pd;
import numpy as np;

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]};

df = pd.DataFrame(data);
df['score2'] = [90,89,98,97];
print(df);
print(df.iloc[0:2,1:3]);

print('---------------------------');
print(df[['score','score2']]);
print(df.loc[1,['score','score2']]);
print(df.loc[0:2,'subject':'students']);
