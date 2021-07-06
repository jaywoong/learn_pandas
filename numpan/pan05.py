import pandas as pd;
import numpy as np;

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]};

print(data);

df = pd.DataFrame(data, columns=['subject', 'score', 'students', 'class']);

df['class2'] = [1,2,3,4];
df.index = ['one','two','three','four'];
print(df);

print(df.columns);
print(df.index);

print(df['subject']);
print(df.subject);

print(df);

# df2 = df[['score','class2']];
# print(df2);

print(df[['subject','score']]);

print(df.loc['two','score':'class']);
print(df.loc['two',['score','students','class2']]);