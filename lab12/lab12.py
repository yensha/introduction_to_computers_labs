import requests
import pymysql
#https://data.gov.tw/dataset/102775(臺南市公有免費停車場)
#從網頁上get json檔
s = requests.get('https://citypark.tainan.gov.tw/App/parking.ashx?verCode=5177E3481D&type=1&ftype=1&exportTo=2')
data_a = s.json()
#取得database連線
db = pymysql.connect(host='localhost', port=3306, user='E94111122', passwd='0219', db='wordpress')
#cursor is used to interact with the database (游標) 
cursor = db.cursor()
#用dictionary的鍵找到value並insert進資料庫
for i in data_a:
      sql = "INSERT INTO 臺南市公有免費停車場(停車場代碼, 停車場名稱, 停車場地址, 停車場型態) VALUES ('" + i["停車場代碼"] + "','" + i["停車場名稱"] + "', '" + i["停車場地址"] + "','"+ i["停車場型態"] +"')"
      cursor.execute(sql)
      #提交修改
      db.commit()

#關閉連線
db.close()
                                        
