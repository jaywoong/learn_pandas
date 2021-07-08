import json

import numpy as np
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
import folium as fol;
from sklearn import preprocessing

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
# titanic
tt = sns.load_dataset('titanic');

# stock
st = pd.read_csv(DATA_DIRS[0]+'//stock-data.csv');

class Part5:
    def p172(self):
        print(tt.info());
        print(tt['deck'].value_counts(dropna=False));
        print(tt.isnull().sum());

        tt1 = tt.dropna(axis=1,thresh=500);
        print(tt1);
        print(tt1.isnull().sum());

        ttage = tt.dropna(subset=['age'], how='any', axis=0);
        print(ttage.isnull().sum());
        print(ttage.info());

    def p178(self):
        mage = tt['age'].mean();
        print(tt['age'].isnull().sum());
        tt['age'].fillna(mage, inplace=True);
        print(tt['age'].isnull().sum());

    def p180(self):
        print(tt.isnull().sum());
        et = tt['embark_town'].value_counts(dropna=True).idxmax();
        print(et);
        tt['embark_town'].fillna(et,inplace=True);
    def p181(self):
        tt['embark_town'].fillna(method='ffill',inplace=True);
    def p186(self):
        print(df3);
        mpg_to_kpl = 1.60934 / 3.78541;
        print(mpg_to_kpl);
        df3['kpl'] = (df3['mpg'] * mpg_to_kpl).round(2);
        print(df3);
    def p188(self):
        print(df3.info());
        print(df3['hor'].unique());
        df3['hor'].replace('?',np.nan, inplace=True);
        print(df3['hor'].unique());
        df3.dropna(subset=['hor'] ,inplace=True);
        print(df3['hor'].unique());
        df3['hor'] = df3['hor'].astype('float');
        print(df3['hor'] );
    def p190(self):
        print(df3.info());
        print(df3['origin'].unique());
        df3['origin'].replace({1:'USA',2:'EU',3:'JPN'},inplace=True);
        print(df3['origin'].unique());
        print(df3['origin'].dtypes);
        df3['origin'] = df3['origin'].astype('category');
        print(df3['origin'].dtypes);
    def p192(self):
        df3['hor'].replace('?',np.nan, inplace=True);
        df3.dropna(subset=['hor'] ,inplace=True);
        df3['hor'] = df3['hor'].astype('float');
        cnt, bin_dividers =np.histogram(df3['hor'],bins=3);
        print(cnt,bin_dividers);

        bin_names = ['고','중','저'];
        df3['hp_bin'] = pd.cut(
            x=df3['hor'],
            bins=bin_dividers,
            labels=bin_names,
            include_lowest=True
        );

        print(df3);
    def p194(self):
        df3['hor'].replace('?', np.nan, inplace=True);
        df3.dropna(subset=['hor'], inplace=True);
        df3['hor'] = df3['hor'].astype('float');
        cnt, bin_dividers = np.histogram(df3['hor'], bins=3);
        print(cnt, bin_dividers);

        bin_names = ['고', '중', '저'];
        df3['hp_bin'] = pd.cut(
            x=df3['hor'],
            bins=bin_dividers,
            labels=bin_names,
            include_lowest=True
        );
        hp_dum = pd.get_dummies(df3['hp_bin']);
        print(hp_dum);
        label_encoder = preprocessing.LabelEncoder();
        onehot_encoder = preprocessing.OneHotEncoder();

        onehot_labeled = label_encoder.fit_transform(df3['hp_bin']);
        print(onehot_labeled);

        onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled),1);
        print(onehot_reshaped);

        onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped);
        print(onehot_fitted);

    def p198(self):
        df3['hor'].replace('?', np.nan, inplace=True);
        df3.dropna(subset=['hor'], inplace=True);
        df3['hor'] = df3['hor'].astype('float');
        print(df3['hor']);
        print(df3['hor'].describe());

        df3['hor'] = df3['hor']/abs(df3['hor'].max());
        print(df3['hor']);

    def p202(self):
        print(st);
        print(st.info());
        st['new_Date'] = pd.to_datetime(st['Date']);
        print(st);
        print(st.info());
        print(st['new_Date'][0])
        st.set_index(st['new_Date'], inplace=True);
        print(st);
    def p205(self):
        datas = ['2019-01-01','2019-03-01','2019-06-01',];
        ts_datas = pd.to_datetime(datas);
        print(ts_datas)
        pr_day = ts_datas.to_period(freq='A');
        print(pr_day);
    def p206(self):
        ts_ms = pd.date_range(
            start='2020-01-01',
            end=None,
            periods=6,
            freq='MS',
            tz='Asia/Seoul'
        );
        print(ts_ms);

        pr_ms = pd.period_range(
            start='2020-01-01',
            end=None,
            periods=6,
            freq='S'
        );
        print(pr_ms);
    def p209(self):

        st['new_Date'] = pd.to_datetime(st['Date']);
        print(st);
        st['Year'] = st['new_Date'].dt.year;
        st['Month'] = st['new_Date'].dt.month;
        st['Day'] = st['new_Date'].dt.day;
        print(st);
        st['Year2'] = st['new_Date'].dt.to_period(freq='A');
        st['Year3'] = st['new_Date'].dt.to_period(freq='M');
        print(st);
        st.set_index(st['Year3'],inplace=True);
        print(st);
    def p212(self):
        st['new_Date'] = pd.to_datetime(st['Date']);
        st.set_index(st['new_Date'],inplace=True);
        print(st);

        st_y = st['2018-06-05':'2018-06-01'];
        print(st_y);

        st_y2 = st.loc['2018-06-05':'2018-06-01','High':'Low'];
        print(st_y2);

        today = pd.to_datetime('2020-07-08');
        st_y2['time_delta'] = today - st_y2.index;
        print(st_y2);


if __name__ == '__main__':
    Part5().p212();




