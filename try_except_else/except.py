# 例外是使用try-except-else程式區塊來處理，try區塊的程式碼是要放可能引起例外的程式碼，如果try的程式區塊執行無誤的話，就會跳到else區塊，而except區塊是放出現指定例外時要處理的程式碼

# * 使用try-except程式區塊

try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero")

# 上面的程式碼如果try區塊沒問題的話就會跳過except區塊，如果try區塊區出錯時就會進入except區塊檢測是否為這個錯誤，並執行其中的程式碼