#建立dictionary存取
dict0 = {}
#用迴圈(先row)將鍵輸入
for n in range(0, 4):
  key = input("Enter key: ")
  value_list = []
  #用迴圈將值輸入
  for k in range(0, 5):
    value = input("Enter value: ")
    value_list.append(value)
    dict0[key] = value_list
#印出整個dictionary
print(dict0)
<<<<<<< HEAD
  

    

=======
>>>>>>> b1048e4b16101298f02e3a88c7d9797f4bf8e427
