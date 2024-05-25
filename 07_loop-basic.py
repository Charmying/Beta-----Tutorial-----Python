# while 迴圈
# 1 + 2 + 3 + ... + 10
n = 1
sum = 0   # 紀錄累加的結果
while n <= 10:
   sum = sum + n
   n += 1
print(sum)   # 55



# for 迴圈
# 1 + 2 + 3 + ... + 10
sum = 0
for x in range(1, 11):
    sum = sum + x
print(sum)   # 55