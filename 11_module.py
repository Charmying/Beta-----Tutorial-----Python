# 建立內建的sys模組並取得資訊
import sys as system
# print(system.platform)   # win32
# print(system.maxsize)   # 9223372036854775807



# 建立 geometry 模組，載入使用
from modules import geometry
result = geometry.distance(1, 1, 5, 5)
# print(result)   # 5.656854249492381
result = geometry.slope(1,2,5,6)
# print(result)   # 1.0



# 調整搜尋模組的路徑
import sys
sys.path.append("modules") # 在模組的搜尋路徑列表中[新增路徑]
print(sys.path)   # 印出模組的搜尋路徑列表

import geometry
print(geometry.distance(1,1,5,5))   # 5.656854249492381