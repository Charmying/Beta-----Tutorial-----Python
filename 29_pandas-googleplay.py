import pandas as pd

# 讀取資料
data = pd.read_csv("googleplaystore.csv")   # 把csv格式的檔案讀取成一個 DataFrame



# 觀察資料
print("資料數量", data.shape)   # 資料數量 (10841, 13)

print("資料欄位", data.columns)
# 資料欄位 Index(['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
#        'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
#        'Android Ver'],
#       dtype='object')



# 分析資料：評分的各種統計數據
condition = data["Rating"] <= 5
data = data[condition]
print("平均數", data["Rating"].mean())   # 平均數 4.191757420456972
print("中位數", data["Rating"].median())   # 中位數 4.3
print("取得前一百個應用程式的平均", data["Rating"].nlargest(1000).mean())   # 取得前一百個應用程式的平均 4.823



# 分析資料：安裝數量的各種統計數據
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "", regex = True).replace("Free", "", regex = True))
print("平均數", data["Installs"].mean())   # 平均數 17897443.726030324

condition = data["Installs"] > 100000
print("安裝數量大於100000的應用程式有幾個", data[condition].shape[0])   # 安裝數量大於100000的應用程式有幾個 4947



# 基於資料的應用：關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字：")
condition = data["App"].str.contains(keyword,case = False)
print("包含關鍵字的應用程式數量", data[condition].shape[0])