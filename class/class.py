# 我們可以使用類別對幾乎任何事物進行塑模，照慣例來說類別的第一個字母為大寫，屬於類別的函式我們稱之為方法，以下的範例我們會提到一個__init__()方法，每當我們以類別建立一個實例的時候，python都會自動執行這個方法，這個方法的開頭和結尾都有兩個底線

class Dog(): # 建立一個Dog類別
    def __init__(self,name,age): 
    # __init__方法我們放了三個參數進去，self是必要的且必須放在其他參數前面，self必須放在定義中是因為python呼叫__init__方法時，方法會自動傳入self引數，每個與類別相關的方法呼叫都會自動傳入self引數
        self.name=name # 取得name參數中的值並將其存入name變數中
        self.age=age # 取得age參數中的值並將其存入age變數中
        # 第三行和第四行這裡所定義的兩個變數名字前面都有self開頭，以self為前導的變數都能提供類別中的所有方法使用，我們也可以由類別所建立的實例來存取這些變數，可用實例來存取的變數就稱之為屬性
    def eat(self): # 定義一個eat方法
        print(self.name + " is eating")
        
    def sleep(self): # 定義一個sleep方法
        print(self.name + " is sleeping")
        
dog1=Dog("tony",3) # 建立一個dog1實例
print("My dog's name is "+dog1.name+" and it's "+str(dog1.age)+" years old.")

dog1.eat() # 呼叫eat方法
dog1.sleep() # 呼叫sleep方法

dog2=Dog("akukin",4)
print(" My dog's name is "+ dog2.name+" and it's "+str(dog2.age)+" years old.")
dog2.sleep()
