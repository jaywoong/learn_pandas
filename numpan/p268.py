import matplotlib.pyplot as plt
import pandas as pd;
import numpy as np;

df = pd.read_csv('./age2.csv',encoding='euc-kr', index_col=0);
df2 = df.div(df.iloc[:,0], axis=0);
df2 = df2.iloc[:,2:];
#print(df2);
#name = input('input location ...?');
name = '신대방제1동';
df_loc = df2[df2.index.str.contains(name)];
print(df_loc);
# 신대방 지역의 데이터 빼기 전체 데이터의 최소값
x = df2.sub(df_loc.iloc[0],axis=1);
x = np.power(x,2);
result = x.sum(axis=1);
result = result.sort_values();
result = result[result > 0];
result = result[:5];
print(result.index);
ddf = df2.loc[result.index];
# 그래프에 신대방제1동까지 표현 하시오
ddf = pd.concat([ddf,df_loc]);
print(ddf);
ddf.T.plot();
plt.show();

















#print(df2.loc[result[:5].index])
# print(df_loc.T);
#
# df_loc.T.plot();
# plt.show();
#print(df_loc.iloc[0,:].to_list());
