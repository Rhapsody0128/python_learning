# 字典和json非常像，但是從本質上講，字典是一種數據結構，而json是一種格式；
# 字典有很多內置函數，有多種調用方法，而json是數據打包的一種格式，並不像字典具備操作性，並且是格式就會有一些形式上的限制，比如json的格式要求必須且只能使用雙引號作為key或者值的邊界符號，不能使用單引號，而且“key”必須使用邊界符（雙引號），但字典就無所謂了。



# * 存取字典中的值
# 在python中字典是一系列的鍵-值對，每一個鍵都有一個對應的值，與鍵相關的可以是數值、串列、也可以是另一個字典，在python中字典是用大括號{ }括住一系列的鍵-值對，鍵和值之間是用冒號來分隔，鍵-值對之間是用逗號分開，如果想存取鍵相關的值，可給定字典的名稱，然後以中括號括住指定的鍵

car = {"color":"black","brand":"Toyota"} # 建立一個car字典裡面包含兩個鍵值對
color = car["color"] # 將car字典中color鍵對應的值存到color變數內
print("The car's color is "+color) # 印出color



# * 新增鍵值對
# 字典是動態的結構，可隨時新增鍵-值對進去，想要新增鍵其實跟存取的方式差不多，用法是給定字典的名稱，然後用中括號括住想要新增鍵的名字，再給定鍵的值

car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
car["mileage"] = 10 # 新增一個鍵為"mileage"值為10到car字典
print(car) # 印出新增鍵值對後的car字典


# * 修改鍵值對
# 修改鍵對應的值一樣需要給定字典名稱，然後使用中括號括住鍵，再把相關聯的新值指定過去即可

car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
car["color"] = "white" # 將car字典中color鍵的值更改成white
print(car) # 印出修改值後的car字典


# * 刪除鍵值對
# 我們是用del陳述句把對應的鍵-值對永久的刪除掉，使用的方法也是跟新增存取一樣，要給定字典的名稱和要刪除的鍵

car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
del car["color"] # 刪除car字典中color鍵和它對應的值
print(car) # 印出刪除值後的car字典


# * 遍訪字典中所有的鍵-值對( items()方法 )
car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
for key,value in car.items(): # items()方法會讓for迴圈將每個鍵-值對分別存到key和value的變數中
    print("key : "+key) # 印出鍵
    print("value : "+value) # 印出值


# * 遍訪字典中所有的鍵( keys()方法 )
car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
for key in car.keys(): # keys()方法會讓for迴圈將每個鍵存到key變數中
    print("key : "+key) # 印出鍵


# * 遍訪字典中所有的值( values()方法 )
car = {"color":"black","brand":"toyota"} # 建立一個car字典裡面包含兩個鍵值對
for value in car.values(): # values()方法會讓for迴圈將每個值存到value變數中
    print("value : "+value) # 印出值


# * 以特定順序遍訪字典的鍵( sorted()方法 )
favorite_fruits={"jack":"banana","rose":"grape","steven":"apple","bonny":"apple"} # 建立一個favorite_fruits字典裡面包含四個鍵值對
for key in sorted(favorite_fruits.keys()): # sorted()方法包住keys()方法會讓for迴圈將每個鍵依照字母順序排好存到key變數中
    print(key) # 印出鍵


# * 刪除重複的值( set()方法 )
favorite_fruits={"bonny":"apple","jack":"banana","rose":"grape","steven":"apple"} # 建立一個favorite_fruits字典裡面包含四個鍵值對(steven和bonny的value都是"apple")
print("the following fruits have been mentioned :")
for value in set(favorite_fruits.values()) : # set()方法包住keys()方法會讓for迴圈將不重複的值存到value變數中
    print(value) # 印出值


# * 字典中的字典
# 建立一個字典裡面包含兩個字典
pets={
  "dog":{
      "name":"Tony",
      "age":4,
      "gender":"male",
  },
  "cat":{
      "name":"Kate",
      "age":3,
      "gender":"female",
  },
} 

for pet,pet_info in pets.items() : # items()方法會讓for迴圈將每個鍵-值對分別存到pet和pet_info的變數中
    print("I have a "+pet+",its name is "+pet_info["name"]+","
    +str(pet_info["age"])+" years old,and gender is "+pet_info["gender"] ) # 分別取得鍵(dog,cat)和從字典中的字典取得值

# * 字典中的串列
colors={"orange":["red","yellow"],"green":["blue","yellow"]} # 建立一個colors字典裡面有兩個鍵值對
    
for keys,values in colors.items() : # items()方法會讓for迴圈將每個鍵-值對分別存到keys和values的變數中
    print("If you want to get color "+keys)
    print("you need to add :")
    for value in values: # 告知python從values串列中取出值，並將取出的值存到value變數內
        print(value)