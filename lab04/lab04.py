#建立三個list分別存取三位學生的成績
student_A = []
student_B = []
student_C = []
print('開始輸入學生A的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:')
#利用迴圈輸入五個成績
for i in range (5):
  num1 = input()
  student_A.append(num1)  
print('A學生成績: ','國文: ', student_A[0], '、英文: ', student_A[1], '、數學: ', student_A[2], '、自然: ', student_A[3], '、社會: ', student_A[4])
print(' ')
print('開始輸入學生B的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:')
for i in range (5):
  num2 = input()
  student_B.append(num2)  
print(' ')
print('B學生成績: ','國文: ', student_B[0], '、英文: ', student_B[1], '、數學: ', student_B[2], '、自然: ', student_B[3], '、社會: ', student_B[4])
print(' ')
print('開始輸入學生C的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:')
for i in range (5):
  num3 = input()
  student_C.append(num3)  
print('C學生成績: ','國文: ', student_C[0], '、英文: ', student_C[1], '、數學: ', student_C[2], '、自然: ', student_C[3], '、社會: ', student_C[4])
print(' ')
#使用sum變數計算平均成績
sum_A = 0
sum_B = 0
sum_C = 0
for i in range (5):
  sum_A = sum_A + int(student_A[i])  
print('A學生平均成績: ', sum_A/5)
for i in range (5):
  sum_B = sum_B + int(student_B[i])  
print('B學生平均成績: ', sum_B/5)
for i in range (5):
  sum_C = sum_C + int(student_C[i])  
print('C學生平均成績: ', sum_C/5)
print(' ')
chi_sum = int(student_A[0]) + int(student_B[0]) +int(student_C[0])
eng_sum = int(student_A[1]) + int(student_B[1]) +int(student_C[1])
math_sum = int(student_A[2]) + int(student_B[2]) +int(student_C[2])
sci_sum = int(student_A[3]) + int(student_B[3]) +int(student_C[3])
soc_sum = int(student_A[4]) + int(student_B[4]) +int(student_C[4])
print('國文平均成績: ', chi_sum/3)
print('英文平均成績: ', eng_sum/3)
print('數學平均成績: ', math_sum/3)
print('自然平均成績: ', sci_sum/3)
print('社會平均成績: ', soc_sum/3)
