# input()函式會讓程式暫停，等待使用者輸入一些文字，python在取得使用者輸入文字後，會把我們輸入的文字存到一個變數內

# * 一般的input()函式
name = input("please enter your name : ")
print("hello,"+name) # 因為name是字串所以可以直接跟"hello,"字串相加f


# * 用int()來取得輸入的字串
age = input("how old are you ?") # 使用者輸入的東西都算是字串
age = int(age) # 將age變數轉成int的型態再傳回age變數中
if age >= 20 : # age變數轉為數值後才可以比大小不然會出錯
    print("can vote")
else :
    print("can't vote")

# * 模術運算子( % )
number = input("please enter a number : ")
number = int(number) # 將number變數轉成int的型態再傳回number變數中

if number % 2 ==0 : # 判斷是否除2會整除
    print("It's even") # 如果整除2就是偶數
else :
    print("It's odd") # 如果們有整除2就是奇數

# 如果是在python 2 的版本中，使用者輸入的方法是用raw_input()函式，用法和python 3 的input()函式相同，都會把接收的輸入解讀成字串


text = "apple banana apple grape apple apple watermelon" # 建立一個text字串
find = input("which word do you want to find ?") # 輸入一個值存到find變數中

print(text.count(find)) # 用count()方法來找find變數的值在text字串裡出現幾次