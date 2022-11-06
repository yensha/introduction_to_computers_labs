import os
path = os.getcwd()
list_path = path.split("/")
del list_path[0]
print(list_path)
word = 'E94111122.txt'
f = open(word, 'w')
x = len(list_path)
for i in range(x):
  f.write(list_path[i]+os.linesep)
path = os.chdir('/home/E94111122/')
menu = os.listdir(path)
print(menu)
y = len(menu)
f.write(os.linesep)
for i in range(y):
  f.write(menu[i]+os.linesep)
f.close()


