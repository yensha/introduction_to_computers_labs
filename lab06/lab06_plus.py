#引入亂數模組
import random as r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
#將1到6名稱變成list
list1 = list(Times.keys())
#用來記錄1-6出現次數
value = list(Times.values())

for i in range(1000000):
  a = r.randint(1, 6)
  if a == 1:
    value[0] = value[0] + 1 
  elif a == 2:
    value[1] = value[1] + 1 
  elif a == 3:
    value[2] = value[2] + 1 
  elif a == 4:
    value[3] = value[3] + 1  
  elif a == 5:
    value[4] = value[4] + 1 
  else:
    value[5] = value[5] + 1 
#取百分比
for j in range (6):
  val = value[j]/10000
  val = round(val, 2)
  print("The probability of", list1[j], "is: ", val, '%')
