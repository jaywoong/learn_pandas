import pandas as pd;
import numpy as np;

datas = np.random.randint(10,100,(6,4));
print(datas);
df = pd.DataFrame(datas);
df.columns = ['score1','score2','score3','score4'];
df.columns = ['s1','s2','s3','s4'];
#df.index = pd.date_range('20210114', periods=6);
print(df);