# 類別中每個屬性都要有初始值，就算這個值是0或空字串都可以，例如在設定預設值時，在__init__方法中指定這初始值是允許的，如果對某個屬性進行了這樣的設定，就無需放入對此屬性提供初始值的參數

class Car():
    def __init__(self,year,brand,color):
        self.year = year
        self.brand = brand
        self.color = color
        self.miles = 0 # 建立一個miles屬性初始值為0
        
    def get_mile(self): # 定義一個get_mile方法可以存取miles
        print("Your "+self.brand+" has "+str(self.miles)+" miles on it")

    def update_mile(self,mileage): # 更新公里數
        self.miles = mileage

    def add_mile(self,kilometer): # 增加公里數
        self.miles += kilometer # 接收一個kilometer值加到self.miles裡
        

car1 = Car(10,"toyota","black") # 建立一個car1實例
car1.get_mile() # 用實例呼叫get_mile方法


# * 直接修改屬性的值

car1.miles = 87 # 使用據點標示法來直接存取並設定出仔的miles屬性
car1.get_mile() # 在car1實例中找出miles屬性並將87指定進去


# * 透過方法修改屬性的值

car1.update_mile(87) # 呼叫update_mile方法並將87當作引數傳入mileage參數中
car1.get_mile()


# * 利用方法進行值的增加
car1.update_mile(8730)
car1.get_mile()

car1.add_mile(9400) # 呼叫add_mile方法並傳入9400
car1.get_mile()