import pandas as pd

data = {
    '수학': [90, 80, 70],
    '영어': [91, 81, 71],
    '과학': [92, 82, 72],
    '국어': [93, 83, 73],
}
df = pd.DataFrame(data, index=['A','B','C'])

class P001:
    def series01(self):
        list_data = ['202007' , 3.14 , 'ABC' , 100 , True]
        sr = pd.Series(list_data)
        print(sr)
        sr2 = sr.tolist()
        print(sr2)
        print(sr.index)
        print(sr.values)
        print(sr[1:3])
    def df01(self):
        print(df)
        df2 = df.copy()
        df2.drop('B', inplace = True)
        print(df2)
    def df02(self):
        print(df)
        df2 = df.copy()
        df2.drop(['영어','국어'], inplace=True, axis=1)
        print(df2)
    def df03(self):
        print(df)
        bdata = df.iloc[[1,2]]
        print(bdata)
    def df04(self):
        print(df)
        df['이름'] = ['영희','철수','민철']
        df.set_index('이름', inplace=True)
        print(df)
        # d1 = df.loc['영희',['국어','수학']]
        d1 = df.iloc[:,0:2]
        print(d1)
    def df05(self):
        print(df)
        df.loc['D'] = [99,88,77,66]
        print(df)
        df2 = df.reset_index()
        print(df2)
        df3 = df2.sort_index(ascending=False)
        print(df3)
        df4 = df2.sort_values(by='수학')
        print(df4)
        # df2 = df.transpose()
        # df2 = df.T

if __name__ == '__main__':
    P001().df05();