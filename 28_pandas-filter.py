# 載入pandas模組
import pandas as pd

# 篩選練習 Series
data = pd.Series([30, 15, 20])
condition = data > 18
print(condition)
# 0     True 
# 1    False 
# 2     True 
# dtype: bool

filteredData = data[condition]
print(filteredData)
# 0    30
# 2    20
# dtype: int64     

data = pd.Series(["酷啦", "Python", "Pandas"])
condition = data.str.contains("P")
print(condition)
# 0    False        
# 1     True        
# 2     True        
# dtype: bool 

filteredData=data[condition]
print(filteredData)
# 1    Python       
# 2    Pandas       
# dtype: object 



# 篩選練習 DataFrame
data = pd.DataFrame({
     "name": ["Amy", "Bob", "Charles"],
     "salary": [30000, 60000, 45000]
})
print(data)
#       name  salary
# 0      Amy   30000
# 1      Bob   60000
# 2  Charles   45000

condition = data["name"] == "Amy"
print(condition)
# 0     True
# 1    False
# 2    False
# Name: name, dtype: bool

filteredData = data[condition]
print(filteredData)
#   name  salary
# 0  Amy   30000