import json

import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
import folium as fol;

from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES


# 인구이동
df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl'
                   ,header=0);
# 전력량
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl');
# auto
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=None);
df3.columns = ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];
# 대학위치
df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');
# 경기도 행정 구역
df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');
# 주가데이터
stock = pd.read_excel(DATA_DIRS[0]+'//stock.xlsx',engine='openpyxl');
# 주식가격
stockp = pd.read_excel(DATA_DIRS[0]+'//stock price.xlsx',engine='openpyxl');
# 주식정보
stockv = pd.read_excel(DATA_DIRS[0]+'//stock valuation.xlsx',engine='openpyxl');
# titanic
tt = sns.load_dataset('titanic');

class Util:
    def add10(self,n):
        return n + 10;
    def add_two(self,a,b):
        return a + b;
    def min_max(self,x):
        return x.max() - x.min();
    def kpl(self,mpg,cyl):
        return mpg * (1.6/3.7) + cyl;
    def m_value(self,x):
        return x.isnull();
    def m_count(self,x):
        return self.m_value(x).sum();
    def total(self,df):
        return self.m_count(df).sum();
    def display(self,df):
        return df.info();
    def zcore(self, x):
        return (x - x.mean())/x.std();

class Part6:
    def p218(self):
        df = tt.loc[:,['age','fare']];
        df['ten'] = 10;
        print(df+ 100);
        df2 = df['age'].apply(Util().add10);
        print(df2);
        df3 = df['age'].apply(Util().add_two,b=20);
        print(df3);
        df['age'] = df['age'].apply(lambda x:Util().add_two(20,x));
        print(df);

    def p221(self):
        #tt.apply(Util().add10);
        df = tt.loc[:,['age','fare']];
        print(df.head());
        df2 = df.apply(Util().add10);
        print(df2.head());
        df3 = df.apply(Util().min_max,axis=1);
        print(df3.head());

        df4 = df.apply(lambda x:Util().add_two(x['age'],x['fare']), axis=1);
        print(df4.head());

    def p221test(self):
        print(df3);
        # df3 df에 kpl이라는 컬럼에 kpl 정보를 입력 하시오
        df3['kpl'] = df3.apply(lambda x:Util().kpl(x['mpg'],x['cyl']), axis=1);
        print(df3);
    def p226(self):
        result = tt.pipe(Util().display);
        print(result);
        result2 = tt.loc[:,['age','fare']].pipe(Util().total);
        print(result2);
    def p229(self):
        df = tt.loc[0:4,'survived':'age'];
        print(df);
        columns = df.columns.values;
        sort_column = sorted(columns);
        df_sort = df[sort_column];
        print(df_sort);


        new_df = df[['sex','age','survived','pclass']];
        print(new_df)
    def p232(self):
        print(stock.info());
        print(stock);
        stock['연월일'] = stock['연월일'].astype('str');
        datas = stock['연월일'].str.split('-');
        print(datas);
        stock['연'] = datas.str.get(0);
        stock['월'] = datas.str.get(1);
        stock['일'] = datas.str.get(2);
        print(stock);
    def p234(self):
        mask = (tt['age'] >= 10) & (tt['age'] < 20);
        mask2 = (tt['age'] >= 10) & (tt['sex'] == 'female');
        mask3 = (tt['age'] < 10) | (tt['age'] > 60)
        tt2 = tt.loc[mask2,['age','sex','pclass']];
        print(tt2);
        pd.set_option('display.max_columns',10);
        mask10 = tt['pclass'] == 1;
        mask20 = tt['pclass'] == 2;
        mask30 = tt['pclass'] == 3;
        tt3 = tt[mask20|mask30];
        print(tt3);

        tt4 = tt['embark_town'].isin(['Southampton','Queenstown']);
        print(tt4);

    def p240(self):
        df1 = pd.DataFrame({
                    'a': ['a0','a1','a2','a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3'],
               },
               index=[0,1,2,3]);
        df2 = pd.DataFrame({
                    #'a': ['a2','a3','a4','a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c5', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5'],
               },
               index=[2,3,4,5]);
        print(df1);
        print(df2);
        result1 = pd.concat([df1,df2],ignore_index=True,join='inner',axis=0);
        print(result1);
        result2 = pd.concat([df1, df2], ignore_index=True,axis=1,join='outer');
        print(result2);

        sr1 = pd.Series(['e0','e1','e2','e3'],name='e');
        sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3,4,5]);
        sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g');
        print(sr2);

        result3 = pd.concat([df1,sr1],axis=1);
        print(result3);
        result4 = pd.concat([df2,sr2],axis=1);
        print(result4);
    def p245(self):
        print(stockp);
        print(stockv);
        df1 = pd.merge(stockp, stockv,on='id', how='inner');
        print(df1);
        df2 = pd.merge(stockp, stockv,how='right',
                       left_on='stock_name',right_on='name');
        print(df2);

        price = stockp[stockp['price'] < 100000];
        print(price);

        value = pd.merge(price,stockv,on='id');
        print(value);

    def p252(self):
        stockp.set_index(stockp['id'],inplace=True);
        stockv.set_index(stockv['id'], inplace=True);
        stockp.drop(['id'],axis=1,inplace=True);
        stockv.drop(['id'], axis=1,inplace=True);
        df3 = stockp.join(stockv, how='inner');
        print(df3);

    def p254(self):
        df = tt.loc[:,['age','sex','class','fare','survived']];
        print(df);
        gdf = df.groupby(['class']);
        print(gdf);
        print(gdf.mean());
        gdf3 = gdf.get_group('Third');
        print(gdf3);

        gdftwo = df.groupby(['class','sex']);
        gdftwo_mean = gdftwo.mean();
        print(gdftwo_mean);

        g1 = gdftwo.get_group(('First','female'));
        print(g1);

    def p261(self):
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']];
        print(df);
        gdf = df.groupby(['class']);
        print(gdf);
        print(gdf.mean());
        print(gdf['fare'].mean());
        # print(gdf.max());
        #
        agg1 = gdf.agg(['mean','min','max']);
        print(agg1);
        #
        agg2 = gdf.agg({'age':['mean'],'fare':['max','min']});
        print(agg2);
        #
        age_zcore = gdf.transform(Util().zcore);
        print(age_zcore);
        #
        # # print(gdf.mean());
        gdff = gdf.filter(lambda x: len(x) > 200);
        print(gdff);
        print(gdff.info());

        # #
        gdff2 = gdf.filter(lambda x: x['age'].mean() < 30);
        print(gdff2);

        # #
        gdfa = gdf.apply(lambda x: x['age'].mean() < 30);
        print(gdfa);
        # #
        age_zcore1 = gdf.transform(Util().zcore);
        age_zcore2 = gdf.apply(Util().zcore);
        print(age_zcore1);
        print(age_zcore2);
    def p271(self):
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']];
        print(df);
        gdf = df.groupby(['class','sex']);
        mgdf = gdf.mean();
        print(mgdf);
        print(mgdf.loc['First','female']);
        print(mgdf.xs('male',level='sex'));
    def p273(self):
        pd.set_option('display.max_columns',10);
        pd.set_option('display.max_colwidth', 20);
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']];
        print(df);
        pdf = pd.pivot_table(df,
                             index='class',
                             columns='sex',
                             values='age',
                             aggfunc=['mean','max']);
        print(pdf);
        pdf2 = pd.pivot_table(df,
                             index=['class','sex'],
                             columns='survived',
                             values=['age','fare'],
                             aggfunc=['mean','max']);
        print(pdf2);
        print(pdf2.xs(('First','female')));
        print(pdf2.xs('male',level='sex'));

        print(pdf2.xs('mean',axis=1))
        print(pdf2.xs(('mean','age'),axis=1))
        print(pdf2.xs(1,level='survived',axis=1))
if __name__ == '__main__':
    Part6().p273();




