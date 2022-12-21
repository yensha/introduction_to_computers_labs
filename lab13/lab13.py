import matplotlib.pyplot as plt 
import numpy as np

f = open('Temperature.txt')
month = list(range(1,13))
m = month #m --> month(1-12)
temp_list = []
year_list = []
f.readline()
for line in f.readlines():
    #將檔案分行讀之後又用逗號切開成str再從map轉成list
    store = list(map(float, line.rstrip("\n").split(",")))
    temp_list.append(store[1:])
    year_list.append(int(store[0]))
f.close

#graph1
m = month
#(12month, all temp, 函數名稱)
for i in range(len(temp_list)):
    plt.plot(m, temp_list[i], label = year_list[i]) 

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.savefig('lab13_01.png')
plt.legend() 
plt.show()

#graph2
#計算每月平均
ave_temp = []
for i in range(len(m)):
    total = 0
    for j in temp_list:
        total += j[i]
    ave_temp.append(round(total/9, 2))#將九年每月的平均值四捨五入到小數點第二位
#畫出九年來每月平均折線圖+點點+換點點以及點點邊緣顏色
plt.plot(m, ave_temp, '-o', markerfacecolor = 'red', markeredgecolor = 'red') 

#算出年平均值四捨五入到小數點第二位
ave = round(sum(ave_temp) / 12, 2)
ave_list = []
for i in range(12):
    ave_list.append(ave)
#畫出九年每月平均虛線
plt.plot(m, ave_list, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
#標出九年每月平均溫度
plt.text(1, ave, ave, va = 'bottom', fontsize = 10)

#使用zip將list壓縮，並用迴圈將數據值印出，標出每個點的value
for i, j in zip(m, ave_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
    
#座標及標題
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')

plt.savefig('lab13_02.png')
plt.legend() 
plt.show()

#graph_assemble
fig = plt.figure(figsize=(15,6))
#(row,clo)-left
plt.subplot(1,2,1)
#graph1
for i in range(len(temp_list)):
    plt.plot(m, temp_list[i], label = year_list[i]) 

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend() 
#(row,clo)-right
plt.subplot(1,2,2)
#graph2
ave_temp = []
for i in range(len(m)):
    total = 0
    for j in temp_list:
        total += j[i]
    ave_temp.append(round(total/9, 2))

plt.plot(m, ave_temp, '-o', markerfacecolor = 'red', markeredgecolor = 'red')  
ave = round(sum(ave_temp) / 12, 2)
ave_list = []
for i in range(12):
    ave_list.append(ave)
plt.plot(m, ave_list, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
plt.text(1, ave, ave, va = 'bottom', fontsize = 10)
for i, j in zip(m, ave_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
#將兩張圖放在一起
fig.suptitle('lab13_finish ', fontsize=16)
plt.tight_layout() #讓子圖之間適當排列不重疊
plt.show()
fig.savefig('lab13_03.png')
