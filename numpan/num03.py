import matplotlib.pyplot as plt;
import numpy as np;

d = [5, 2, 4, 5, 6, 7];
nd = np.array(d);
nnd = np.sort(nd)[::-1];
print(nnd[0:3]);