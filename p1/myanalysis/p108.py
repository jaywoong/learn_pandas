import pandas as pd;
import numpy as np;
from matplotlib import pyplot as plt

from config.settings import DATA_DIRS


class P108:
    def p108(self):
        df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',
                           engine='openpyxl',header=0);
        #print(df);
        df = df.fillna(method='ffill');
        print(df);
        mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시');
        df_seoul = df[mask];
        df_seoul = df_seoul.drop('전출지별',axis=1);
        df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True);
        df_seoul.set_index('전입지',inplace=True);
        sr_one = df_seoul.loc['경기도'];
        result = [];
        d = {};
        d['name'] = '경기도';
        d['data'] = sr_one.values.tolist();
        result.append(d);
        return result;



if __name__ == '__main__':
    P108().p108();