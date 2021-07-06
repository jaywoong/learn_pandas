import pandas as pd;

from config.settings import DATA_DIRS

df = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv');
df.columns = ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];

ddf = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl');

class P084:
    def df01(self):
        print(df.head(10));
        print(df.shape);
        print(df.info());
        print(df.dtypes);
        print(df.describe(include='all'));
    def df02(self):
        uv = df['origin'].value_counts();
        print(uv);
        df2 = df[['mpg','wei']].mean();
        print(df2);
        df3 = df[(df['mpg'] > df['mpg'].mean()) & (df['mpg'] < 20)];
        print(df3);

    def df03(self):
        print(ddf);
        ddf2 = ddf.iloc[[0,5],3:];
        print(ddf2);
        ddf2.index = ['south','north'];
        print(ddf2);
        ddf2.columns = ddf2.columns.map(int);
        ddf2t = ddf2.T;
        print(ddf2t);
if __name__ == '__main__':
    P084().df03();