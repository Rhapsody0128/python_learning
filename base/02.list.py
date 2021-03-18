# 「串列」是個依照特定順序排放的項目集合所組成，在python中串列是用中括號[ ]來表示，而串列中的個別元素是以逗號來分隔

fruits=["apple","banana","grape","pineapple"]
print(fruits)
print(fruits[0])
print(fruits[-2])
# 索引值也可以是負數，負數的意思是從後面數回來 ! 所以索引值-1的意思是倒數第一個元素，索引值-2的意思是倒數第二個元素，索引值-3的意思是倒署第三個元素...以此類推
fruits.append("mango")
fruits.append("lemon")
print(fruits)
# append()方法是從串列尾端新增一個元素進去

fruits.insert(3,"orange")
print(fruits)
# insert()方法是可以在串列的任一位置新增元素，用法是指定插入新元素的索引值位置和值即可

fruits[0] = "badapple"
print(fruits)
# 要修改串列中的某個元素，必須先指定串列名稱和想要修改項目元素的索引值位置，再指定新的值進去即可


del fruits[0]
print(fruits)
# 知道元素是在哪一個位置(索引值)，就可以使用del陳述句來刪除元素


fruits.pop()
print(fruits)
# pop()方法是源自於"堆疊"，中文解釋是彈出的意思，將串列想像成堆疊的樣子，而pop()方法就是把堆疊最頂端的東西彈出來，堆疊的最頂端是最後加進去的元素，也就是說pop()方法是刪除串列尾端的項目

value = fruits.pop(1)
print(value)
print(fruits)

# 如果知道元素的索引值，就可以任意pop()出想要的值

value = "orange"
fruits.remove(value)
print(fruits)

# 有時候我們不知道元素的索引值是多少但又想要刪除它的時候，我們可以使用remove()方法，它是一個可以依據值來刪除元素的方法，如果只是想要暫時刪除串列中的元素，我們可以先定義一個變數來儲存要刪除的值，然後再用remove()刪除它

fruits.sort()
# 「串列」是個依照特定順序排放的項目集合所組成，在python中串列是用中括號[ ]來表示，而串列中的個別元素是以逗號來分隔

fruits=["apple","banana","grape","pineapple"]
print(fruits)
print(fruits[0])
print(fruits[-2])
# 索引值也可以是負數，負數的意思是從後面數回來 ! 所以索引值-1的意思是倒數第一個元素，索引值-2的意思是倒數第二個元素，索引值-3的意思是倒署第三個元素...以此類推
fruits.append("mango")
fruits.append("lemon")
print(fruits)
# append()方法是從串列尾端新增一個元素進去

fruits.insert(3,"orange")
print(fruits)
# insert()方法是可以在串列的任一位置新增元素，用法是指定插入新元素的索引值位置和值即可

fruits[0] = "badapple"
print(fruits)
# 要修改串列中的某個元素，必須先指定串列名稱和想要修改項目元素的索引值位置，再指定新的值進去即可


del fruits[0]
print(fruits)
# 知道元素是在哪一個位置(索引值)，就可以使用del陳述句來刪除元素


fruits.pop()
print(fruits)
# pop()方法是源自於"堆疊"，中文解釋是彈出的意思，將串列想像成堆疊的樣子，而pop()方法就是把堆疊最頂端的東西彈出來，堆疊的最頂端是最後加進去的元素，也就是說pop()方法是刪除串列尾端的項目

value = fruits.pop(1)
print(value)
print(fruits)

# 如果知道元素的索引值，就可以任意pop()出想要的值

value = "orange"
fruits.remove(value)
print(fruits)

# 有時候我們不知道元素的索引值是多少但又想要刪除它的時候，我們可以使用remove()方法，它是一個可以依據值來刪除元素的方法，如果只是想要暫時刪除串列中的元素，我們可以先定義一個變數來儲存要刪除的值，然後再用remove()刪除它

fruits.sort()
print(fruits)

# sort()方法可以讓串列按字母順序排序，但是是永久性的改變排列順序

fruits.sort(reverse=True)
print(fruits)
# 如果想要讓串列依字母相反順序排序的話，要在sort()方法中傳入reverse=True參數

value = sorted(fruits)
print(fruits)
print(value)

value = sorted(fruits,reverse=True)
print(value)
# sorted()方法跟sort()方法很像，不過sorted()方法是可以暫時性的改變排列順序，不會影響原串列的排列順序