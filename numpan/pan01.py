import numpy as np
import pandas as pd;

# python list
data = [1,2,3,4,5];

# numpy
ndata = np.array(data);

# pandas
pdata = pd.Series(data);
print(pdata[0]);
print(pdata.values);
print(pdata.index);

pdata2 = pd.Series(data, index=['A','B','C','D','E']);
print(pdata2);
print(pdata2['C']);

# dic
data2 = {'name':'kim','ko':100,'en':90,'ma':80, 'si':100};
pdata3 = pd.Series(data2);

pdata3.name = 'Score Name';
pdata3.index.name = 'Score Index name';
print(pdata3);
print(pdata3['name']);
print(pdata3.ko);







