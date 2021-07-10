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
# titanic
tt = sns.load_dataset('titanic');

class Part5:
    def p172(self):
        '';
if __name__ == '__main__':
    Part5().p172();




