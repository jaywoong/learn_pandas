import pandas as pd;
import numpy as np;

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

# 2. james3의 점수를 출력 하시오
print(df.loc['james3']);
print(df.iloc[2]);
# 3. ko 점수가 90점 이상인 학생의 정보를 출력 하시오
print(df[df['ko'] > 90]);
print(df.loc[df['ko'] > 90]);
# 4. ko 점수가 90점 이상인 학생의 이름과 en 점수를 출력 하시오
print(df.loc[df['ko'] > 90 ,'en']);
print(df.loc[df['ko'] > 90 ,['en','si']]);
# 5. james4의 ma, si  점수만 출력 하시오
print(df.loc['james4',['ma','si']]);
print(df.iloc[3,2:4]);
# 6.df를 df2 로 복사하여 en 점수가 90점 미만인 학생의 점수는 모두 90점으로 변경 하시오
df2 = df.copy();
df2.loc[df['en'] < 90 , 'en'] = 90;
print(df2);