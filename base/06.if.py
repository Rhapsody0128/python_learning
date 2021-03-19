age=21 # 定義一個變數值為20

if age>=20 : # 判斷變數值是否大於20
  print("can vote") # 若大於20印出can vote
else : # 變數值沒有大於20就執行else區塊
  print("can't vote") # 進入else區塊後印出can't vote

names=["bonny","jack","rose"] # 建立一個names串列

for name in names : # 告知python從names串列中取出名字，並將取出的名字存到name變數中
  if name=="bonny" : # 判斷如果name等於bonny
      print(name.upper()) #等於bonny就把bonny變全部大寫 
  else : # 如果name不等於bonny
    print(name) #不等於bonny就直接把name印出




a = 5
b = 6
c = 4

if a>c and b>a : # a>c和b>a都是正確敘述，所以會跳到下一行印出句子
  print("Both conditions are True")
# 用and檢測
# 用and關鍵字把每個條件連起來，如果每個條件都是True的話整條條件式就為True，但只要有一個條件沒通過，整個條件式就會是False


if a>c or b<a :  # a>c是正確敘述，b<a是錯誤敘述，但因為or只要其中一個條件正確就可以通過，所以會跳到下一行印出句子
  print("At least one of the conditions are True")
# 用or檢測
# 用or關鍵字把每個條件連起來，它和and不同的是，or只要一個條件是True就可以讓整個條件式為True，or關鍵字只會在全部的條件是False的時候，才會讓整個條件式是False


card="gold" # 定義card變數是gold

if card=="gold" : 
  print("30% off") # 如果card等於gold印出打7折
elif card=="silver" :
  print("20% off") # 如果card等於silver印出打8折
else :
  print("10% off") # 如果不是gold也不是silver則印出打9折

score=87

if score==100 :
  print("A+") # score等於100印出A+
elif 90<=score<100 :
  print("A") # score介於90~99印出A
elif 80<=score<90 :
  print("B") # score介於80~89印出B
elif 70<=score<80 :
  print("C") # score介於70~79印出C
elif 60<=score<70 :
  print("D") # score介於60~69印出D
else :
  print("F") # score不在以上範圍內印出F

# 這個部分是要來講解if陳述句其實不只有if-else這種寫法，當我們需要檢測超過兩種以上的條件時，我們可以用到if-elif-else，python只會執行if-elif-else路徑中的一個程式區塊，它會依序檢測每個條件，直到碰到符合條件的檢測，在通過檢測後，python才會執行緊接在後面的程式區塊，並跳過其他剩下的檢測



# 到目前為止我們對每個檢測都做了簡單的假設，那就是串列中至少有一個項目，隨後我們要讓使用者輸入資訊來存放到串列內，因此不能再假設每次迴圈執行時串列不是空的，因此我們在執行for迴圈前檢測串列是否為空的非常重要

# 檢測串列是否為空
scores=[] # 建立一個空的scores串列

if scores : # 如果串列裡有東西
  for score in scores : # 將scores串列裡的值一一存取到score變數內
    print(score) # 一一印出score變數的值
  print("completed!!") # 最後印出completed!!
else :
  print("list is empty") # 若串列是空的就跳到else區塊然後印出這行
# 因為串列值是空的，所以會直接跳到else區塊，如果不是空的話就會進入if區塊去跑for迴圈



# 想要檢測這個值是否不在串列內時，我們可以使用not in關鍵字來協助，當然的如果想檢測這個值是否在串列內時，我們只要使用in關鍵字就好

# 檢測某值是否不在串列中

letters=["a","c","d"] # 建立一個letters串列
letter="b" # 建立一個letter變數

if letter not in letters : # 判斷letter的值是否不在letters串列裡
  print(letter," is not in list") # 若不在串列內則印出這行


# * print默認是印出一行，结尾加換行。end=""的意思是結尾加空格不換行
for i in range(1, 9): # i從1到9
  for j in range(1, 9): # j從1到9
    print(j ,'*', i ,'=' ,i*j," ",end="")  #印出i*j=i*j  
  print("\n") # 換行

for i in range(1,8,2): # i從1開始到7間隔是2(所以是跑1,3,5,7)
  for j in range(i): # j在i的範圍內(ex:當i=1時，j=1/ i=3時，j=1,2,3/ i=5時,j=1,2,3,4,5)
    print("*",end="") # 印出*
  print() # 換行