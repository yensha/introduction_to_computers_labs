#建立dictionary存取
dict0 = {
  "index":['國文', '英文', '數學', '自然', '社會'], "STUA":[50, 60, 70, 80, 90], "STUB":[57, 86, 73, 82, 43], "STUC":[97, 96, 86, 97, 83]
}
#印出整個dictionary
print(dict0)
#方便取名字
stu_name = ['A', 'B', 'c']
#dict_values以list()轉換成串列，才可以使用索引方式取得元素值
score = list(dict0.values())
#用迴圈得出分數
#二維表格
#國文 英文 數學 自然 社會
# 50  60  70  80   90...
for i in range(1,4):
  total = sum(score[i])/5
  print(stu_name[i-1], "學生平均成績: ", total)
for j in range(0,5):
  ave = (score[1][j]+score[2][j]+score[3][j])/3
  print(score[0][j], "的平均分數: ", ave)
    
  

    
<<<<<<< HEAD

=======
>>>>>>> b1048e4b16101298f02e3a88c7d9797f4bf8e427
