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

# 子類別ElectriCar
class ElectricCar(Car): # 定義一個子類別，且括號內一定要放入父類別
    def __init__(self,year,brand,color): # 接收Car實例所需要的資訊
        super().__init__(year,brand,color) # 這行會使python呼叫ElectricCar父類別的__init__()方法，讓ElectricCar實例含有父類別的所有屬性

        self.battery_size = 100 # 新增一個屬性初始值為100
        
    def get_battery(self): # 新增一個get_battery方法
        print("Your "+self.brand+" has "+str(self.battery_size)+"-KWh battery")


ecar1 = ElectricCar(2018,"toyota","black")
ecar1.get_name()
ecar1.get_battery()


# 覆寫父類別的方法
# 如果父類別的方法不符合子類別的需求，我們都可以覆寫，其作法是在子類別中定義一個與父類別方法有相同名稱的方法，這樣pythoon就不會去用父類別同名的方法，只會關注子類別中定義的這個方法

class AnotherElectricCar(Car):
    def __init__(self,year,brand,color): 
        super().__init__(year,brand,color)
        self.battery_size = 100 
        
    def get_battery(self): 
        print("Your "+self.brand+" has "+str(self.battery_size)+"-KWh battery")
        
    def fill_gas(self): # 覆寫父類別的fill_gas方法
        print("This car doesn't need a gas tank")
        
ecar2 = AnotherElectricCar(2018,"toyota","black")
ecar2.get_name()
ecar2.get_battery()
ecar2.fill_gas()