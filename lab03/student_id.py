#設定變數 n 紀錄
n = input('please input a number:')
#將輸入值變為整數
number = int(n)
#if-else判斷式用除以二餘式判斷奇偶
if number%2 == 0:
  print('it is even')
else:
  print('it is odd')
#設定m、id為變數紀錄學號
m = input('please input your student ID first character:')
id =input('please input your student ID last 8 number:')
#將輸入值id變為整數
new_id = int(id)
#在用上述if-else判斷式用除以二餘式判斷奇偶
if new_id%2 == 0:
  print('your student ID is even')
else:
  print('your student ID is odd')
#輸出學號
print('your student ID is:', m+id)
  