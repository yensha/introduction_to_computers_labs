#想不到遞迴要怎模不改到數據輸出所以函式好長qq
def gcb (a, b):
  if a == 0 or b == 0:
    print("0沒有gcb")
    return 0
#用另外兩個變數儲存傳入值，不會變動原本數據
#定i為比較大的那個
  elif a < b:
    i = b
    j = a
  else:
    i = a
    j = b
#輾轉相除法，用stro儲存不然會變動到i,j
  while j != 0:
    stro = i%j
    i = j
    j = stro
  if i == 1:
    print(a, "和", b,"互質")
  else:
    print(a, "和",b ,"的gcb是 = ", i)
#call函式   
ans1 = gcb(80, 20)
ans2 = gcb(10, 0)
ans3 = gcb(19, 20)
