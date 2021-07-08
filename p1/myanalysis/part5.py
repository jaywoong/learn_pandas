import json

import numpy as np
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
import folium as fol;

from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',header=0);
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl');
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=None);
df3.columns = ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];
df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');
df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');
tt = sns.load_dataset('titanic');

class Part5:
    def p172(self):
        print(tt.info())
        print(tt['deck'].value_counts(dropna=False))
        print(tt.isnull().sum())

        tt1 = tt.dropna(axis=1, thresh=500)
        print(tt1)
        print(tt1.isnull().sum())

        ttage = tt.dropna(subset=['age'], how='any', axis=0)
        print(ttage.isnull().sum())

    def p178(self):
        mage = tt['age'].mean()
        print(tt['age'].isnull().sum())
        tt['age'].fillna(mage, inplace=True)
        print(tt['age'].isnull().sum())

    def p180(self):
        print(tt.isnull().sum())
        et = tt['embark_town'].value_counts(dropna=True).idxmax()
        print(et)
        tt['embark_town'].fillna(et,inplace=True)
        print(tt['embark_town'])

    def p181(self):
        tt['embark_town'].fillna(method='ffill',inplace=True)

    def p186(self):
        print(df3)
        mpg_to_kpl = 1.60934 / 3.78541
        print(mpg_to_kpl)
        df3['kpl'] = df3['mpg'] * mpg_to_kpl.round(2)
        print(df3)

    def p188(self):
        print(df3.info())
        print(df3['hor'].unique())
        df3['hor'].replace('?',np.nan, inplace=True)
        print(df3['hor'].unique())
        df3['hor'] = df3['hor'].astype('float')
        print(df3['hor'])

if __name__ == '__main__':
    Part5().p188()