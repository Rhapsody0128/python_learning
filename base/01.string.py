s='hello'
print(s)

student_name=" gary  "
school="TSHighSchool"
student_id= 405570147
print(student_name.title())
print(student_name.upper())
print(student_name.lower())
print(len(student_name))
print(school+" "+student_name)
print(school+student_name)
print(school+" "+str(student_id)+" "+student_name.lstrip().rstrip() + str(student_id))
print(student_name.lstrip().rstrip())

# 第一行是在定義一個student_name變數是"Weiting"字串
# 第二行是在定義一個school變數是"FJU"字串
# 第三行是在定義一個student_id變數是405570147，但資料型態是int(整數)
# 第四行的title()方法是讓第一個字大寫
# 第五行的upper()方法是讓全部變大寫
# 第六行的lower()方法是讓全部變小寫
# 第七行的len()方法是計算長度
# 第八行是兩個字串的相加(中間還有再加一個空格隔開兩個字串)
# 第九行是兩個字串相加(可以和第八行比較一下輸出結果)。
# 第十行是字串和int的相加，因為字串只能跟字串相加，所以int要轉成字串的型態，不然會出現TypeError(型別錯誤) ! str()方法是轉成字串的意思 !
# 第十一行是將去除左邊再清除右邊的空白的字串存回變數中

# • title()---讓第一個字大寫
# • upper()---讓全部變大寫
# • lower()---讓全部變小寫
# • len()---計算長度
# • \n---換行
# • \t ---空格
# • lstrip()刪除左邊空白、
# • rstrip()刪除右邊空白
# • strip()刪除兩邊空白
# • #---註釋