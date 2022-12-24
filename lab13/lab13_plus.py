import matplotlib.pyplot as plt 
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


f = open('oddExperiment.txt')
f.readline()
x = []
y = []
for line in f.readlines():
    #將檔案分行讀之後又用逗號切開成str再從map轉成list
    s = list(map(float, line.rstrip("\n").split(" ")))
    x.append(s[1])
    y.append(s[0])
f.close

fig = plt.figure()
plt.scatter(x, y, label = 'Data')
first = np.polyfit(x, y, 1)
pf = np.poly1d(first)
yvals_1=pf(x)
lse_1= round(mean_squared_error(y, yvals_1), 5)#lse
r1 = round(r2_score(y, yvals_1), 5)#R^2 error

second = np.polyfit(x, y, 2)
ps = np.poly1d(second)
yvals_2=ps(x)
lse_2 = round(mean_squared_error(y, yvals_2), 5)#lse
r2 = round(r2_score(y, yvals_2), 5)#R^2 error

plt.plot(x, yvals_1, color = '#EDB120', label = "Fit of degree 1, LSE = "+ str(lse_1))
plt.plot(x, yvals_2, color = 'green', label = "Fit of degree 2, LSE = "+ str(lse_2))
plt.plot(x, yvals_1, color = 'red',label="Fit of degree 1, R2 = "+ str(r1))
plt.plot(x, yvals_2, color = '#7E2F8E',label="Fit of degree 2, R2 = "+ str(r2))

plt.title('OddExperiment Data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('lab13_plus.png')
plt.show()
