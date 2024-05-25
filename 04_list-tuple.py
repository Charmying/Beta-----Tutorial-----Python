# 有序可變動列表 List
grades = [12, 60, 15, 70, 90]
print(grades)   # [12, 60, 15, 70, 90]

# 連續刪除列表中從編號 1 到編號 4(不包括)的資料
grades[1:4] = []
print(grades)   # [12, 90]

# 可輕易做列表的串接
grades = grades + [12, 33]
print(grades)   # [12, 90, 12, 33]

# 取得列表的長度 len(列表資料)
length = len(grades)
print(length)   # 4

# 把 55 放到列表中的第一個位置
grades[0] = 55
print(grades)   # [55, 90, 12, 33]



# 槽狀列表
data = [[3, 4, 5], [6, 7, 8]]
print(data)   # [[3, 4, 5], [6, 7, 8]]

# 此動作為更動資料(新資料取代舊資料)，Tuple 資料不可以更動
data[0][0:2]=[5, 5, 5]
print(data)   # [[5, 5, 5, 5], [6, 7, 8]]



# 有序不可變動列表 Tuple
data = (3, 4, 5)
data[0] = 5   # Error：Tuple的資料不可以變動
print(data)