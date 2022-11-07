#import os 模組
import os
#得到當前工作目錄(string)
path = os.getcwd()
list_path = path.split("/")
#delet space
del list_path[0]
#print 當前工作目錄(list)
print(list_path)
#建立txt檔
word = 'E94111122.txt'
#write in txt
f = open(word, 'w')
x = len(list_path)
for i in range(x):
  f.write(list_path[i]+os.linesep)
#找回/home/E94111122
path = os.chdir('/home/E94111122/')
#print 當前目錄下所有檔案和資料夾
menu = os.listdir(path)
print(menu)
y = len(menu)
#write in txt
f.write(os.linesep)
for i in range(y):
  f.write(menu[i]+os.linesep)
f.close()


