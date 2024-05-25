# 載入pandas模組
import pandas as pd

# 資料索引：pd.DataFrame(字典,index=索引列表)
data = pd.DataFrame({
    "name": ["Amy", "Bob", "Charles"],
    "salary": [30000, 60000, 45000]
},index=["a", "b", "c"])
print(data)
#       name  salary
# a      Amy   30000
# b      Bob   60000
# c  Charles   45000



# 觀察資料
print("資料數列", data.size)   # 資料數列 6
print("資料形狀(列、欄)", data.shape)   # 資料形狀(列、欄) (3, 2)
print("資料索引", data.index)   # 資料索引 Index(['a', 'b', 'c'], dtype='object')



# 取得列(Row / 橫向)的 Series 資料：根據順序、根據索引
print("取得第二列", data.iloc[1], sep = "\n")
# 取得第二列
# name        Bob
# salary    60000
# Name: b, dtype: object

print("取得第 c 列", data.loc["c"], sep = "\n")
# 取得第 c 列
# name      Charles
# salary      45000
# Name: c, dtype: object



# 取得欄(Column / 直向)的 Series 資料：根據欄位的名稱
print("取得 name 欄位", data["name"], sep = "\n")
# 取得 name 欄位
# a        Amy
# b        Bob
# c    Charles
# Name: name, dtype: object



# 取得單維度的Series資料
names = data["name"]
print("把 name 全部轉大寫", names.str.upper(), sep = "\n")
# 把 name 全部轉大寫
# a        AMY
# b        BOB
# c    CHARLES
# Name: name, dtype: object



# 計算薪水的平均值
salaries = data["salary"]
print("薪水的平均值", salaries.mean())
# 薪水的平均值 45000.0



# 建立新的欄位
data["revenue"] = [5000000, 4000000, 3000000]   # data[新欄位的名稱] = 列表
data["rank"] = pd.Series([3, 6, 1], index = ["a", "b", "c"])   # data[新欄位的名稱] = Series的資料
data["cp"] = data["revenue"] / data["salary"]
print(data)
#       name  salary  revenue  rank          cp
# a      Amy   30000  5000000     3  166.666667
# b      Bob   60000  4000000     6   66.666667
# c  Charles   45000  3000000     1   66.666667