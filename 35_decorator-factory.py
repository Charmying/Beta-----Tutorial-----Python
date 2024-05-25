# 計算 1 + 2 + 3 + ... + max 的裝飾器工廠
def calculateFactory(max):
    def calculate(callback):
        def run():
            total = 0
            for n in range(max + 1):
                total += n
            callback(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("計算結果是", result)   # 計算結果是 5050

@calculateFactory(10)
def showEnglish(result):
    print("Result is", result)   # Result is 55

show()
showEnglish()



def myFactory(base):
    def myDeco(cb):
        def run():
            print("裝飾器內的程式", base)   # 裝飾器內的程式 10
            result = base * 2
            cb(result)
        return run
    return myDeco

@myFactory(10)
def test(result):
    print("普通函式的程式", result)   # 普通函式的程式 20

test()