import numpy as np;

ldata = [1,2,3,4,5];
print(ldata);
print(type(ldata));
print(ldata[2:]);

ndata = np.array(ldata);
print(ndata);
print(type(ndata));
print(ndata[2:]);

a = np.eye(5);
print(a);

#print(ldata + 5);
print(ndata / 5);
ndatas = np.sqrt(ndata);
print(ndatas);

ndata2 = np.zeros(5);
print(ndata2 + 6);


ndata3 = np.arange(-5,5);
print(ndata3);
print(ndata3 >  2);
print(ndata3[ndata3  > 2]);

data1 = [10,9,33,88,66,55,40];

ndata1 = np.array(data1);
result = ndata1[ndata1 > 50];
print(result);
# 짝수만 result2에 추츨 하시오
result2 = ndata1[ndata1 % 2 == 0];
print(result2);
result3 = result2.tolist();
print(result3);


