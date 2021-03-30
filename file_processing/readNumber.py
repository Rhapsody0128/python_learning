import random

with open("file_processing/number.txt") as file_object: # 開啟number.txt檔並將其存到file_object中
    content=file_object.read() # 讀取file_object的所有內容
    print(content.rstrip()) # 將印出的檔案刪除read()返回的一行空白

with open("file_processing/number.txt") as file_object: 
  for line in file_object: 
      print(line)

with open("file_processing/number.txt","w") as file_object: # 以寫入模式開啟number.txt檔
		a = str(int(random.random()*10000))
		with open("file_processing/TEST.py") as H :
			b = H.read()
			file_object.write(a+'\n') # 寫入第一行
			file_object.write(b) # 寫入第二行
			
			print("第一行寫入了"+a)
			print("第二行寫入了"+b)