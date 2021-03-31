# # 例外是使用try-except-else程式區塊來處理，try區塊的程式碼是要放可能引起例外的程式碼，如果try的程式區塊執行無誤的話，就會跳到else區塊，而except區塊是放出現指定例外時要處理的程式碼

# # * 使用try-except程式區塊

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

# # 上面的程式碼如果try區塊沒問題的話就會跳過except區塊，如果try區塊區出錯時就會進入except區塊檢測是否為這個錯誤，並執行其中的程式碼


# # * 使用try-except-else程式區塊

# # 以下的範例是處理ZeroDivisionError例外的try-except-else程式碼

# while True:
#     first=input("First number :")
#     second=input("Second number :")
#     try:
#         ans=int(first)/int(second) # 因為input都是字串所以要轉int才能相除
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         print(ans) # 若沒有出錯就印出兩個值相除
#         break # 跳出迴圈

# # 上面的程式碼如果second輸入0，進入到try時計算出ZeroDivisionError (X/0 = 無限大)，出錯跳到except，跳過else再次進入While迴圈
# # 上面的程式碼如果計算成功，直接跳到else印出答案並跳出while迴圈


# while True :
#     try:
#         filename = input("請找出正確的檔案: ")
#         fullFilename=f"try_except_else/{filename}.txt"
#         with open(fullFilename) as file:
#             contents=file.read()
#     except FileNotFoundError: # 如果找不到檔案會執行這個區塊
#         msg="Sorry,the file '"+filename+"' does not exist"
#         print(msg)
#     else: # 找到檔案會執行這個區塊
#         print(contents)
#         break


# 以下的範例是處理FileNotFoundError例外的try-except-else程式碼，當我們找不到檔案時會印出一行訊息告知使用者檔案找不到，找的到檔案的話就讀取檔案內容，然後到else區塊讓使用者輸入要找的字，然後計算總共在alice.txt檔中出現幾次
filename=input("請輸入alice文本: ")
fullFuleName = f"try_except_else/{filename}.txt"
try:
    with open(fullFuleName) as file:
        contents=file.read()
except FileNotFoundError: # 如果找不到檔案會執行這個區塊
    pass
    # 用pass可以讓此區塊的直接跳過
    msg="Sorry,the file '"+filename+"' does not exist"
    print(msg)
else: # 找到檔案會執行這個區塊
    find=input("請入問要找文本內的單字 :")
    print('出現'+str(contents.count(find))+'次')