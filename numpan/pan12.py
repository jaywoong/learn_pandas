import pandas as pd;
import numpy as np;

data = [[1.4, np.nan], [8.3, -2.1], [0.02, -1.11], [np.nan, np.nan]];
x = pd.DataFrame(data, columns=['one', 'two'], index=['a', 'b', 'c', 'd']);

print(x);
print('------------------');
print(x.sum());
print(x.sum(axis=0,skipna=False));
print(x.sum(axis=1,skipna=False));
print('------------------');
print(x['one'].sum());
print(x.loc['a'].sum());
print('------------------');
print(x.mean());
print(x.mean(axis=1));
print('------------------------------------------------');

data = {
    'name':['james1','james2','james3','james4','james5'],
    'ko':[100,90,89,99,89],
    'en':[99,91,87,89,81],
    'ma':[80,92,88,99,87],
    'si':[99,100,87,93,86],
};

df = pd.DataFrame(data);
print(df);

# 1. 인덱스 값을 이름으로 변경 하시오
df.index = data['name'];
print(df);
del df['name'];
print(df);

# 학생 별 합(sum), 평균(avg) 컬럼을 추가 한다.
# 과목 별 합(sum), 평균(avg) row를 추가 한다.
new_df = df.copy();
new_df['sum'] = new_df.iloc[:,0:4].sum(axis=1);
new_df['avg'] = new_df.iloc[:,0:4].mean(axis=1);
print('-----');
new_df.loc['sum'] = new_df.iloc[0:new_df.shape[0],:].sum();
new_df.loc['avg'] = new_df.iloc[0:new_df.shape[0]-1,:].mean();
print(new_df);

# 국어 평균 점수 보다 높은 학생들을 조회 하시오
print(df);
df2 = df[df['ko'] > df['ko'].mean()];
print(df2);


# df2 = df[df['ko'] > df.loc['avg'][0]];
# df2 = df2.drop('sum',axis=0);
# print(df2);
# 전체 평균 보다 높은 학생들을 조회 하시오
# df3 = df[df['avg'] > df.loc['avg'][5]];
# df3 = df3.drop('sum',axis=0);
# print(df3);

print('------------------------------------------');
print(df);
print(df.min());
print(df.max());
print(df.min(axis=1));
print(df.max(axis=1));
print(df.idxmin());
print(df.idxmax());

df5 = df.idxmax();
df5 = pd.DataFrame(df5,columns=['name']);
df5['score'] = df.max();
print(df5);

# dic 만들어 보자
dic1 = {df5.columns[0]:df5['name'].tolist(),
        df5.columns[1]:df5['score'].tolist()};

print(dic1);

