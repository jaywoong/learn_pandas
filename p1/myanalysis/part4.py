import pandas as pd
import matplotlib.pyplot as plt

from config.settings import DATA_DIRS, STATICFILES_DIRS

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl', header=0);
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl');

class P109:
    def mat01(self):
        df2 = df.fillna(method='ffill')
        print(df2)
        mask = (df2['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
        df_seoul = df2[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        sr_one = df_seoul.loc['경기도']
        print(sr_one)
        plt.plot(sr_one)
        plt.title('서울 -> 경기')
        plt.savefig(STATICFILES_DIRS[0]+'/ss.jpg')
        plt.show()

    def mat02(self):
        df2 = df.fillna(method='ffill')
        print(df2)
        mask = (df2['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
        df_seoul = df2[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        df3 = df_seoul.loc[['경상북도','강원도','충청북도','전라남도']]
        print(df3)
        # df3.loc['sum'] = df3.sum()
        df3['sum'] = df3.sum(axis=1)
        print(df3)
        df3s = df3[['sum']].sort_values(by='sum')
        print(df3s)

        # df3t = df3.T
        # print(df3t)
        # plt.style.use('ggplot')
        # df3t.index = df3t.index.map(int)
        # df3t.plot(kind='area', stacked=False, alpha=0.2, figsize=(10,5))
        # plt.show()

    # def mat03(self):


if __name__ == '__main__':
    P109().mat01();
