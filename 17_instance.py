# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

# 建立第一個實體物件
p1 = Point(3, 4)
print(p1.x, p1.y)   # 3 4
# 建立第二個實體物件
p2 = Point(5, 6)
print(p2.x, p2.y)   # 5 6



# FullName實體物件的設計：分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = FullName("韋翰","真的")
print(name1.first, name1.last)   # 韋翰 真的
name2=FullName("好", "雞掰")
print(name2.first,name2.last)   # 好 雞掰