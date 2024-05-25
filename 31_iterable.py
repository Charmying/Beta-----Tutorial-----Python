# Iterable 資料型態
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代的資料:
dic = {"a": 3, "x": 5}
for key in dic:
    print(key)
    print(dic[key])
# a
# 3
# x
# 5



# 內建函式
# max(可疊代資料)
result = max([10, 2, 30, 1])
print(result)   # 30
result = max("xaz")
print(result)   # z
result = max({10, 200, 30, 1})
print(result)   # 200
result = max({"x": 3, "a": 4})
print(result)   # x

# sorted(可疊代資料)
result = sorted("cab")
print(result)   # ['a', 'b', 'c']
result = sorted({10, 2, 100, -5})
print(result)   # [-5, 2, 10, 100]