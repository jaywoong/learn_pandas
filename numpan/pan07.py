import pandas as pd;
import numpy as np;

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]};

df = pd.DataFrame(data);

print(df);

df2 = df[df['score'] > 90];
print(df2[['score','students']]);

print(df.loc[df['score'] > 90,['score','students']]);

print('--------------------------------------------');
df3 = df.copy();
print(df3);
df3.loc[df3['score'] > 90 , 'score'] = 200;
print(df3);


