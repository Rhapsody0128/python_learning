from car import Car # import陳述句會讓python開啟car模組並匯入Car類別
from car import Car,ElectricCar # import陳述句會讓python開啟car模組並匯入Car和Electric類別


car1 = Car(2018,"toyota","black") 
car1.get_name() 

car1 = Car(2018,"toyota","black") 
car1.get_name()
car1.update_mile(87)
car1.get_mile()

ecar1 = ElectricCar(2019,"benz","white")
ecar1.get_name()
ecar1.get_battery()