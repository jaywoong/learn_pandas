import pandas as pd;
import numpy as np;

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]};
df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class']);
print(df);
#df['class'] = [1,2,3,4];
df2 = df.copy();
df2.index = ['a','b','c','d'];
data = [5,6,7,8];
ser1 = pd.Series(data);
ser1.index = df2.index;
print(ser1);
df2['class'] = ser1;
print(df2);

print('----------------------');
df2['pass'] = (df2['score'] >=90 );
df2['average'] = [96.4,np.NaN,77.6,98.0];
print(df2);
df3 = df2.dropna();
print(df3);
df4 = df2.fillna(value=0);
print(df4);






