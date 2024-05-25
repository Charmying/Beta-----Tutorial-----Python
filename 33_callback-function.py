def add(n1, n2, cb):
	cb(n1 + n2)

def handle1(result):
	print("結果是", result)

def handle2(result):
	print("Result of Add is", result)

add(3, 4, handle1)   # 結果是 7
add(5, 6, handle1)   # 結果是 11
add(4, 2, handle2)   # Result of Add is 6



def test(arg):
	arg("Hello")   # 呼叫回呼函式，帶入參數

# 定義一個回呼函式
def handle(da):
	print(da)   # Hello

test(handle)