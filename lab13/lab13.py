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
#(12month, all temp, 函數名稱)
for i in range(len(temp_list)):
    plt.plot(m, temp_list[i], label = year_list[i]) 
#使用xtick/ytick函式標定刻度    
plt.xticks(m)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc = 'lower center') 
plt.show()
plt.savefig('lab13_01.png')
#graph2
#計算每月平均
ave_temp = []
all_t = 0
for i in range(len(m)):
    total = 0
    for j in temp_list:
        total += j[i]
    all_t += total
    ave_temp.append(round(total/9, 2))#將九年每月的平均值四捨五入到小數點第二位
    
#畫出九年來每月平均折線圖+散佈圖+換點點顏色
plt.scatter(m, ave_temp, color = 'red')
plt.plot(m, ave_temp) 

#算出年平均值四捨五入到小數點第二位
ave = round((all_t /108), 2)
ave_list = []
for i in range(12):
    ave_list.append(ave)
#畫出九年每月平均虛線
plt.axhline(y=ave, xmin=0, xmax=13, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
#標出九年每月平均溫度
plt.text(1, ave, ave, va = 'bottom', fontsize = 10)

#使用zip將list壓縮，並用迴圈將數據值印出，標出每個點的value
for i, j in zip(m, ave_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
    
#座標及標題
plt.xticks(m)
plt.yticks(range(16,34,2))
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
    
plt.xticks(m)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc = 'lower center') 

#(row,clo)-right
plt.subplot(1,2,2)
#graph2
ave_temp = []
all_t = 0
for i in range(len(m)):
    total = 0
    for j in temp_list:
        total += j[i]
    all_t += total
    ave_temp.append(round(total/9, 2))#將九年每月的平均值四捨五入到小數點第二位
#畫出九年來每月平均折線圖+散佈圖+換點點顏色

plt.scatter(m, ave_temp, color = 'red')
plt.plot(m, ave_temp) 

#算出年平均值四捨五入到小數點第二位
ave = round((all_t /108), 2)
ave_list = []
for i in range(12):
    ave_list.append(ave)
#畫出九年每月平均虛線
plt.axhline(y=ave, xmin=0, xmax=13, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
#標出九年每月平均溫度
plt.text(1, ave, ave, va = 'bottom', fontsize = 10)

#使用zip將list壓縮，並用迴圈將數據值印出，標出每個點的value
for i, j in zip(m, ave_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
    
#座標及標題
plt.xticks(m)
plt.yticks(range(16,34,2))
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.savefig('lab13_02.png')
plt.legend() 

#將兩張圖放在一起
fig.suptitle('lab13_finish ', fontsize=13)
plt.tight_layout() #讓子圖之間適當排列不重疊
plt.show()
fig.savefig('lab13_03.png')
