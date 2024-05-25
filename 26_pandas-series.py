# 載入 pandas 模組
import pandas as pd

# 資料索引
data = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])
print(data)
# a    5      
# b    4      
# c   -2      
# d    3      
# e    7      
# dtype: int64



# 觀察資料
print("資料型態", data.dtype)   # 資料型態 int64
print("資料數量", data.size)   # 資料數量 5 
print("資料索引", data.index)   # 資料索引 Index(['a', 'b', 'c', 'd', 'e'], dtype='object')



# 取得資料：根據順序、根據索引
print(data[2], data[0])   # -2 5
print(data["e"], data["d"])   # 7 3



# 數字運算：基本、統計、順序
print("最大值",data.max())   # 最大值 7
print("總和",data.sum())   # 總和 17
print("標準差",data.std())   # 標準差 3.361547262794322
print("中位數",data.median())   # 中位數 4.0
print("最大的三個數",data.nlargest(3))   # data.nsmallest(2)：最小的兩個數
# 最大的三個數 e    7
# a    5
# b    4
# dtype: int64



# 字串運算：基本、串接、搜尋、取代
data = pd.Series(["酷啦", "Python", "Pandas"])
print(data.str.lower())   # 全部變小寫
# 0        酷啦
# 1    python
# 2    pandas
# dtype: object

print(data.str.len())   # 算出每個字串的長度
# 0    2
# 1    6
# 2    6
# dtype: int64

print(data.str.cat(sep = "-"))   # 把字串串起來，可以自訂串接的符號
# 酷啦-Python-Pandas

print(data.str.contains("酷"))   # 判斷每個字串是否包含特定的字元
# 0     True
# 1    False
# 2    False
# dtype: bool

print(data.str.replace("酷啦","好胖"))
# 0        好胖
# 1    Python
# 2    Pandas
# dtype: object