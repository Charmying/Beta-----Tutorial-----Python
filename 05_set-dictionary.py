# 集合的運算
s1 = {3, 4, 5}
print(10 not in s1)   # True

s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
# 交集：取兩個集合中相同的資料
s3 = s1 & s2
print(s3)   # {4, 5}
# 聯集：取兩個集合中的所有資料，但不重複取
s4 = s1 | s2
print(s4)   # {3, 4, 5, 6, 7}
# 差集：從 s1 中減去和 s2 重疊的資料
s5 = s1 - s2
print(s5)   # {3}
#反交集：取兩交集中不重疊的資料
s6 = s1 ^ s2
print(s6)   # {3, 6, 7}

s = set("Hello")   #把字串中的字母拆解成集合：set(字串)
print("A" in s)   # False



# 字典的運算：key-value 配對 
dic = {"apple": "蘋果","bug": "蟲蟲"}
dic["apple"] = "小蘋果"
print(dic["apple"])   # 小蘋果

#判斷key是否存在
print("test" not in dic)   # True

dic = {"apple": "蘋果","bug": "蟲蟲"}
print(dic)   # {'apple': '蘋果', 'bug': '蟲蟲'}

# 刪除字典中的鍵值對(key-value pair)
del dic["apple"] 
print(dic)   # {'bug': '蟲蟲'}

# 從列表的資料產生字典
dic={x: x * 2 for x in [3, 4, 5]}
print(dic)   # {3: 6, 4: 8, 5: 10}