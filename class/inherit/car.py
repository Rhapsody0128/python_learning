# python第一個要進行工作是把值分配給父類別的所有屬性，父類別一定要放在目前的程式檔案內，且放置位置要在子類別的前面，super()是特殊的函式會協助python把父類別和子類別連接起來

class Car():
    def __init__(self,year,brand,color):
        self.year = year
        self.brand = brand
        self.color = color
        self.miles = 0
    def get_name(self): # 印出名字
        print(str(self.year) +" "+ self.brand)

    def get_mile(self): # 存取公里數
        print("Your "+self.brand+" has "+str(self.miles)+" miles on it")
        
    def update_mile(self,mileage): # 更新公里數
        self.miles = mileage
        
    def add_mile(self,kilometer): # 增加公里數
        self.miles += kilometer
        
    def fill_gas(self): # 車子加油
        print("This car need a gas tank")

class ElectricCar(Car): # 定義一個子類別，且括號內一定要放入父類別
    def __init__(self,year,brand,color): # 接收Car實例所需要的資訊
        super().__init__(year,brand,color) # 這行會使python呼叫ElectricCar父類別的__init__()方法，讓ElectricCar實例含有父類別的所有屬性

        self.battery_size = 100 # 新增一個屬性初始值為100
        
    def get_battery(self): # 新增一個get_battery方法
        print("Your "+self.brand+" has "+str(self.battery_size)+"-KWh battery")