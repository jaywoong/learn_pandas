import pandas as pd;
import numpy as np;

x1 = pd.DataFrame(np.random.randint(10, 100, (3, 4)),
                  columns = list('ABCD'), index = list('abc'));
x2 = pd.DataFrame(np.random.randint(10, 100, (3, 4)),
                  columns = list('ABCD'), index = list('def'));
print(x1);
print(x2);

x3 = pd.concat([x1,x2],ignore_index=True);
dt = pd.date_range('20210614', periods=6);
x3.index = dt;
x3['F'] = [1,2,3,4,5,6];
print(x3);