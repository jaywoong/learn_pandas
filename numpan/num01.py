import random
import numpy as np;
import matplotlib.pyplot as plt;

r1 = random.randint(1,10);
r2 = np.random.randint(1,10);

print(r1);
print(r2);

rnums = np.random.choice(10,6, replace=False);
print(rnums);

dice = np.random.choice(6,10);
print(dice);


plt.hist(list, bins=6);
plt.show();