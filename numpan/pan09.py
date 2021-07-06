import pandas as pd;
import numpy as np;

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]};
df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class']);
df.index = ['one','two','three','four'];
print(df);
print(df.shape, df.shape[0]);

df2 = pd.DataFrame(data);
new_df = df2.copy();

print(df2);
df2.loc[df2.shape[0]] = ['korea',80,78];
print(df2);
df2.loc['total'] = ['eng',99,89];
print(df2);
df2['score2'] = [99,88,99,77,66,44];
print(df2);

del df2['subject'];
print(df2);

df3 = df2.drop('students',axis=1);
print(df3);

df4 = df2.drop(['score','score2'],axis=1);
print(df4);

df5 = df2.drop('total', axis=0);
print(df5);

print(new_df);

print(new_df['score'].tolist());
print(new_df.loc[2].tolist());
print(new_df['score'].to_numpy());