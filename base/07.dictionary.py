# 字典和json非常像，但是從本質上講，字典是一種數據結構，而json是一種格式；
# 字典有很多內置函數，有多種調用方法，而json是數據打包的一種格式，並不像字典具備操作性，並且是格式就會有一些形式上的限制，比如json的格式要求必須且只能使用雙引號作為key或者值的邊界符號，不能使用單引號，而且“key”必須使用邊界符（雙引號），但字典就無所謂了。
a = {
  "a":1,
  "b":2,
  "c":3
}
print(a["a"])

import json
aa = json.loads(json)
print(aa)
