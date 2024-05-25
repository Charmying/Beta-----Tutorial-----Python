# pip install pandas

# 載入pandas模組
import pandas as pd



# 建立Series
data = pd.Series([20, 10, 15])

# 基本Series操作
# print(data)
# 0    20
# 1    10
# 2    15
# dtype: int64

# print("Max", data.max())   # Max 20
# print("Median", data.median())   # Median 15.0

data = data * 2
#print(data)
# 0    40
# 1    20
# 2    30
# dtype: int64

data = data == 20
# print(data)
# 0    False
# 1     True
# 2    False
# dtype: bool



# 建立 DataFrame
data = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "salary": [80000, 60000, 55000]
})

# 基本DataFrame操作
print(data)
#    name  salary
# 0   Amy   80000
# 1  John   60000
# 2   Bob   55000

# 取得特定的欄位
print(data["salary"])
# 0    80000
# 1    60000
# 2    55000

# 取得特定的列
print(data)
#    name  salary
# 0   Amy   80000
# 1  John   60000
# 2   Bob   55000

print(data.iloc[1])   # 印出第二列
# name       John
# salary    60000
# Name: 1, dtype: object