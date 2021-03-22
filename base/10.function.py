# 函式是個取了名字的程式區塊，專們用來完成特定的工作，當我們要執行函式時，可以呼叫函式的名字來完成工作，若需要在一個程式中執行同一項工作很多次，那我們不需要一直寫重複的程式碼，我們只需要呼叫函式來幫我們完成工作

# * 定義函式
# 我們需要用到def關鍵字來告知python我們要定義一個函式

def hello_world(): # 定義一個hello_world()函式
    print("hello world") # 函式的工作是印出hello world

hello_world() # 呼叫hello_world()函式


# * 把資訊傳入函式內
# 做法是在我們已經定義的函式括號內放入參數，藉由放入參數來接收我們在呼叫函式時所傳入的任意值

def greet(name): # 在greet函式放入name去接收任意值，在這裡是接收到"Weiting"
    print("hello,"+name)
    
greet("Weiting") # 呼叫greet()函式


# * 傳入引數
# 在函式中定義的變數是參數，被函式呼叫的是引數，因為函式定義可以有多個參數，所以呼叫函式也可能需要多個引數，我們可以使用位置引數和關鍵字引數

# * 位置引數
# 位置引數是編寫順序要和參數的順序相同，每個引數都要對應到函式定義的參數，如果引數位置順序不對的話，程式不會出錯，但輸出的結果可能不是我們想要的 ! 所以要檢查好引數和參數有沒有對應好

def pets(pet_name,pet_type): # 定義pets函式需要兩個引數
    print("I have a "+pet_type+" and its name is "+pet_name)

#以下是函式的多次呼叫，只要在呼叫一次函式它就會印出對應的值
pets("dog","tony") # 將dog引數放入pet_type參數中、tony引數放入pet_name參數中
pets("cat","candy")


# * 關鍵字引數
# 關鍵字引數是傳入函式的名-值對，它不像位置引數需要考慮位置順序有沒有一致，我們只需要明確的指出函式中定義的參數名字

def pets(pet_name,pet_type): 
    print("I have a "+pet_type+" and its name is "+pet_name)
    
# 將pet_name和pet_type交換也是沒關係的，對應的值對了就好
pets(pet_type="dog",pet_name="tony") # 明確的指出pet_type對應dog、pet_name對應tony 
pets(pet_name="candy",pet_type="cat") 


# * 先給定預設值
# 可以先給定參數一個預設值，如果在呼叫函式時沒給值的話，就會用預設值來處理

def pets(pet_name,pet_type="dog"): 
    print("I have a "+pet_type+" and its name is "+pet_name)

pets(pet_name="tony") # 預設pet_type是dog所以只要傳入pet_name就好
pets(pet_name="candy",pet_type="cat") # 如果不是dog的話就傳入新的pet_type它就不會使用預設值



# * 返回簡單值
# 函式返回的值我們稱之為返回值，用法是用return陳述句把值返回到呼叫函式的那行程式碼中

def get_location(city,area,zipcode): # 定義一個get_location函式需要三個引數
    location=city+" "+area+" "+zipcode
    return location # 返回location

return_value=get_location("新北市","新莊區","242") # 把返回值指定存放在return_value變數中
print(return_value)


# * 返回字典
# 函式能夠返回各種型別的值，包括串列、字典等比較複雜的資料結構

def get_name(first_name,last_name): # get_name函式接收first_name和last_name
    name={"first":first_name,"last":last_name} # 將收到的first_name值對應到first鍵，將last_name值存到last鍵，再將兩的鍵值對存到name字典
    return name # 返回name字典

return_value=get_name("bonny","chang")
print(return_value)


# * 傳入串列

def get_name(names):
    for name in names:
        print("hello,"+name)
        
usernames=["bonny","steven","jack","rose"]
get_name(usernames) # 將usernames串列傳入get_name函式中


# * while迴圈使用函式
def get_name(first_name,last_name):
    name=first_name+" "+last_name
    return name

while True:
    print("enter 'q' at any time to quit") # 新增一條文字告知使用者如何隨時跳出迴圈
    
    first=input("enter your first name :")
    if first =="q": # 當使用者輸入"q"則跳出迴圈
        break
    last=input("enter your last name :")
    if last =="q": # 當使用者輸入"q"則跳出迴圈
        break
        
    print(get_name(first,last)) # 呼叫get_name函式接收輸入的first值和last值


# * 傳入任意數量的引數到函式
# 有時候我們不知道函式預先需要接收多少個引數，這時候我可以使用一個星號來建立空多元組，或兩個星號建立空字典，我們就先直接來看範例吧 !

# * 一個星號(建立空多元組)

def get_name(*names): # "*"+names參數中的星號會讓python建立一個名字為names的空多元組
    for name in names:
        print("hello,"+name)
    
get_name("bonny","steven")
get_name("jack")
get_name("rose","john","jane")

# 如果上述的程式碼沒有for迴圈那行，那麼程式碼就會出錯，因為for迴圈的工作是把多元組裡的值一一輸出出來，所以如果沒有for迴圈那行而直接印出的話，是印出多元組而不是印出接收到的字串值，多元組是不能跟字串相加的，所以它會跑出下列這種錯誤