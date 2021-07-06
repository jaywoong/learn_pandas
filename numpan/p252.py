import pandas as pd;
import numpy as np;

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0,index_col=0);
#print(df[1]);
summer = df[1].iloc[1:,:5];
summer.columns = ['경기수','금','은','동','합계'];
sort_summer = summer.sort_values('금', ascending=False);
sort_summer.to_csv('./summer.csv',sep=',');
print(sort_summer.iloc[:21,:]);