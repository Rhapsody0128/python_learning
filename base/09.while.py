# while迴圈和for迴圈不一樣的是，for迴圈收集項目的集合，並對集合中的每個項目執行一次程式區塊，而while迴圈在條件為真時會一直不斷地執行

number = 1
while number < 6 : # 當number<6的時候
    print(number) # 印出number
    number = number + 1 # number加一後再存回number中
    #number = number + 1 也可以寫成 number += 1


# break敘述 & continue敘述
# 那如果說我們想要讓使用者自己決定結束的時間呢 ? 這時我們就要定義一個結束值，當使用者輸入結束值時，程式就會結束

# break敘述與continue敘述
# 1.對於迴圈想要擁有更高的控制性
# 2.利用break在任何時候跳出迴圈
# 3.利用continue會返回迴圈的開頭，並檢測條件再判斷要不要繼續執行迴圈

# * break
text = "enter your name or enter 'quit' to leave the program : "
while True : # 讓迴圈一直執行
    name = input(text) # 印出text字串將輸入的值存到name變數中
    
    if name == "quit" : # 當輸入quit時進入if區塊
        break # 跳出迴圈
    else :
        print("Hello,"+name)  

# * continue
number = 0
while number < 10 : # 當number<10就會繼續跑迴圈
    number += 1 
    if number % 3 != 0: # 判斷number是否不能被3整除
        continue # 如果不能被3整除就跳回迴圈一開始再加1
    
    print(number) # 如果可以被3整除就印出數字


# 我們在串列那單元提到for迴圈，for迴圈對串列來說是很有效的工具，但for迴圈卻不能修改串列，不然python會很難處理其中的項目，想要遍訪串列又想要修改串列的話，我們就必續用到while迴圈來處理


# * 從某個串列般一項目到另一個串列
# 我們可以用來點餐，將點餐的餐點一一存到要煮的串列中，煮好後再一一的輸出出來

order=["hamburger","french fries","cola"]
already_cooked=[]

while order : # 如果order串列有東西while迴圈就會繼續執行
    cooking=order.pop() # 將order串列的值一一彈出來存到cooking變數中
    print("cooking :"+cooking)
    already_cooked.append(cooking) # 將cooking變數的值新增到already_cooked串列中

print("Finished :")
for cooked in already_cooked : # 告知python從already_cooked串列中取出值，並將取出的值存到cooked變數中

    print(cooked)


# * 刪除串列中含有特定值的所有項目
# 之前我們有提到remove()方法可以刪除特定的值，但remove()能夠順利運作是因為該值在串列只出現一次，當要刪除的值出現很多次的時候，我們就要用while迴圈

text = ["apple", "banana", "apple", "grape", "apple", "apple", "watermelon"]

while "apple" in text : # 當text串列中含有apple字串時，迴圈就會一直執行
    text.remove("apple") # 將text串列中的apple字串移除

print(text)


# * while迴圈處理字典
# 我們可以以使用者輸入的方式來把值填入字典中
response={} # 建立一個空字典

while True:
    name=input("What's your name?")
    place=input("Where would you want to go?")
    response[name]=place # 建立name為鍵place為值的鍵-值對然後存到response字典中

    continue_prompt = input("Would you like to let someone else respond? (yes/no)")
    if continue_prompt=="no": # 如果continue_prompt=="no"就跳出迴圈
        break
    
for name,place in response.items(): # items()方法會讓for迴圈將每個鍵-值對分別存到name和place的變數中
    print(name+" would like to go "+place)