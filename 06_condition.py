# 判斷式
# x = input("請輸入數字：")   # 取得字串形式的使用者輸入
# x = int(x)   # 將字串型態轉換成數字型態
# if x > 100:
#    print("大於 100")
# elif x > 50:
#    print("大於 50，小於等於 100")
# else:
#    print("小於等於 50")



# 四則運算
n1 = float(input("請輸入第一個數字："))
calculate = input("請輸入運算：+ or - or * or /：")
n2 = float(input("請輸入第二個數字："))
if calculate == "+":
    print("Ans：", n1 + n2)
elif calculate == "-":
    print("Ans：", n1 - n2)
elif calculate == "*":
    print("Ans：", n1 * n2)
elif calculate == "/":
    print("Ans：", n1 / n2)
else:
    print("不支援運算")