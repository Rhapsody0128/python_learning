# 在使用者關閉程式時，我們都會希望把這些資訊保存下來，今天我們會用到json模組來儲存資料，json模組能讓我們把簡單的python資料結構轉成到檔案內，並在再次執行的時候載入檔案的資料

# * 儲存

# json.dump( )的使用方法是它會接收兩個引數，第一個是儲存的資料，第二個是用來儲存資料的檔案物件

import json

numbers=[1,2,3,4,5,6] 

filename="file_processing/number.json" # 指定要把numbers串列存到number.json檔中
with open(filename,"w") as file: # 以寫入模式開啟檔案才可以將資料儲存進去
    json.dump(numbers,file) # 將numbers串列存到number.json檔


# * 載入

# 現在我們在編寫一隻程式，使用json.load( )把numbers串列獨到記憶體內

with open(filename) as file: # 以讀取模式開啟檔案(若沒有第二個參數都是預設成讀取模式)
    numbers=json.load(file) # 用json.load()載入放在number.json檔裡面的資料，然後將它存到numbers變數中

print(numbers)



filename="file_processing/username.json"

try:
    # 在try中放json.load()是因為如果username.json檔已經存在的話，就直接將名字載入記憶體中
    with open(filename) as file: 
        username=json.load(file)
except FileNotFoundError:
    # 如果檔案找不到時我們會提供使用者輸入訊息並寫入檔案中以便再開啟時可以紀錄原先輸入的名字
    username=input("What's your name ?")
    with open(filename,"w") as file:
        json.dump(username,file)
        print("We'll remember you when you come back,"+username)
else:
    print("Welcome back,"+username)