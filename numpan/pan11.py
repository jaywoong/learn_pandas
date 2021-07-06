import pandas as pd;
import numpy as np;

data = [1,2,3,4];
print(data * 2);

n1 = np.array(data);
print(n1 + 2);

p1 = pd.Series(data);
print(p1);

p2 = p1.copy();
p2[4] = 10;
print(p1 / p2);

print('----------------------------------------');

x = pd.DataFrame(np.arange(12).reshape(3, 4), columns = list('abcd'));
print(x);
xx = x.loc[1];
print(x.add(xx)); # x + xx
print(x + [9,9,9,9]);











