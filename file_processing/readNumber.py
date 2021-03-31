import random


# * 讀取整個檔案

# 我們會用到open()函式接收一個引數，引數就是放想要開啟的檔案名稱，python會在目前執行的檔案所在的資料夾中尋找檔案，然後存到一個變數中，而read()方法會讀取整個檔案的內容，但是read()到達檔案尾端時會返回一行空字串，這時我們就可以用到第二天教的rstrip()刪除右邊空白來處理 !
with open("file_processing/number.txt") as file_object: # 開啟number.txt檔並將其存到file_object中
    content=file_object.read() # 讀取file_object的所有內容
    print(content.rstrip()) # 將印出的檔案刪除read()返回的一行空白

with open("file_processing/number.txt") as file_object: 
  for line in file_object: 
      print(line)


# * 讀取整個檔案
# 當我們把文字寫入檔案後，就算關掉顯示程式輸出的終端視窗，輸出的結果還是會保存，這時我們呼叫open()需要放入兩個引數，第一個引數是要開啟的檔案名，第二個引數是要告知python以甚麼模式來開啟檔案


#    w				 r			  a					 r+
# 讀取模式	寫入模式	附加檔案	可讀取寫入模式


# 如果想要寫入的檔案不存在，open()函式會自動建立，不過以寫入模式有一點要注意，如果要寫入的檔案已經存在的話，python會自動清空檔案的內容，再將寫入的文字傳進去

with open("file_processing/number.txt","w") as file_object: # 以寫入模式開啟number.txt檔
		a = str(int(random.random()*10000))
		# p.s python只能把字串寫入文字檔中，要把數值資料儲存到文字檔中，必須先使用str()函式轉換成字串
		with open("file_processing/TEST.py") as H :
			b = H.read()
			file_object.write(a+'\n') # 寫入第一行
			file_object.write(b) # 寫入第二行
			
			print("第一行寫入了"+a)
			print("第二行寫入了"+b)

for i in range(2) :
	a = str(int(random.random()*10000))
	with open(f"file_processing/{a}.txt",'w') as test :
		test.write(a)


