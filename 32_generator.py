# 定義建立生成器函式
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10



# 呼叫並回傳生成器
gen = test()



# 搭配for迴圈中使用
for d in gen:
    print(d)
# 階段一
# 5     
# 階段二
# 10   



def generateEven(maxNumber):
    number = 0
    while number <= maxNumber:
        yield number
        number += 2

evenGenerator = generateEven(16)
for data in evenGenerator:
    print(data)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
