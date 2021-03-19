for number in range(1,7):
  print(number)

rangeTest = range(1,7)
print(rangeTest)
print(range(1,7))

# range()函式會讓python從指定的第一個值開始算起，到指定的第二個值就停止，因此輸出並不含第二個值

# 若是要讓數字存到串列中，可以使用list()函式把range()函式的結果直接轉成串列，用法是把range()函式當成參數包在list()函式裡

odd_numbers=list(range(1,10,2))
print(odd_numbers)

# 上面這段程式碼是要印出1~10之間的奇數，第一行程式碼的range(1,10,2)是在說建立一個從1開始間隔是2到10就停止的數列，然後再用list()函式包住range()函式，使range()函式建立出來的數列變成數字串列，第二行就是把值印出

