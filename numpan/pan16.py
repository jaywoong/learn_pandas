import pandas as pd;
import numpy as np;

x1 = pd.Series([0, 1, 2]);
x2 = pd.Series([3, 4, 5]);
x3 = pd.Series([6, 7, 8]);
x4 = pd.concat([x1, x2, x3],axis=1,keys=list('abc'));
print(x4);

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns = list('ABCD'), index = np.arange(3));
df2 = pd.concat([x4['a'],df1],axis=1,ignore_index=True);
df2.columns = ['a','b','c','d','e'];
print(df2);
df3 = pd.concat([df1,x4['a']]);
print(df3);