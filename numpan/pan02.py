import numpy as np
import pandas as pd;

data = np.arange(0,5);
print(data);
idx = ['b','a','c','e','d'];
pdata = pd.Series(data,index=idx);
#print(pdata[pdata > 0]);
print(pdata);
pdata2 = pdata.reindex(np.sort(np.array(idx)));
print(pdata2);
idx.append('x');
idx.append('y');
pdata3 = pdata.reindex(idx,fill_value=0);
print(pdata3);
print(np.average(pdata3));



