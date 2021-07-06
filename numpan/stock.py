import pandas as pd;
import numpy as np;

df = pd.read_html('https://finance.naver.com/sise/lastsearch2.nhn',
                  encoding='euc-kr');
stock = df[1].dropna();
stock.index = stock['순위'];
del stock['순위'];

# stock = stock.sort_values(by='등락률',ascending=False);
# print(stock['등락률']);
