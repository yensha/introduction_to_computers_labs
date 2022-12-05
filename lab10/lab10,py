from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#用一個全域dictionary去記錄所有的keys跟values
store_dic = {}
# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def root():
    return 'ok' # 發送response body 為 ok
# 設定路由為/set
# 使用 request.form 來接收body的資料，接著用to_dict()這個function來轉成python的dict格式，就可以使用這個資料了
#data中的value則會是我所要的[鍵-值]
@app.route('/set',methods=['POST'])
def food():
    data = request.form.to_dict()
    #將data中的鍵與值取出並傳成list,[0]是鍵,[1]是值
    get_value = list(data.values())
    if get_value[0] in store_dic:
        return 'key exist'
    else:
        store_dic[get_value[0]] = get_value[1]
        return 'set success'
@app.route('/key_list',methods=['GET'])
def cook():
    #將鍵全部取出並轉成str
    x = list(store_dic.keys())
    return str(x)
#key做為路由變數傳入找尋指定key
@app.route('/get_value/<key>',methods=['GET'])
def book(key):
    if key in store_dic:
        return store_dic[key]
    else:
        return 'key not found'
#從網站輸入update的資料並換上
@app.route('/update_value',methods=['POST'])
def foot():
    data = request.form.to_dict()
    get_value = list(data.values())
    if get_value[0] in store_dic:
        store_dic[get_value[0]] = get_value[1]
        return'update success'
    else:
        return'key does not exist'
#key做為路由變數傳入找尋指定key, 刪掉指定的鍵
@app.route('/delete/<key>',methods=['GET'])
def mood(key):
    if key in store_dic:
        del store_dic[key]
        return 'delete success'
    else:
        return 'key not found'
# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)
