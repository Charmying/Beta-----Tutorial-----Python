# Python 筆記

[Python 入門教學課程](https://www.youtube.com/playlist?list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk)



###### <br/>

---

###### <br/>



## 快速開始 <br/> 01_start.py

1. 在 D 槽建立新資料夾 (python)

2. 於 VS Code 的左上方工具列找到檔案 → 開啟資料夾 → 找到 D 槽建立的資料夾 (Python)

3. 新增檔案，主檔名 隨便 (建議英文)，副檔名為 .py

4. 切到終端機 (TERMINAL)

5. 執行 → python 1_start.py → `enter`

- 若要清空 TERMINAL 畫面 → cls `enter`

- 註解：程式碼內打 #，# 後面可任意加寫文字，不會影響程式執行

###### <br/>
###### <br/>
###### <br/>





## 變數 & 資料 & 資料型態 <br/> 02_datatype.py

- 資料：程式中最基本的單位

- 資料型態 (Data type)：資料的分類

- 資料的分類

	- 數字：整數、長整數、浮點數(小數)

	- 字串：任意的文字內容

	- 布林值：表達正確 (True) 或錯誤 (False)，T&F需大寫

	- 可變列表 (List)：有順序、可變動的資料集合，ex. 學生的成績

	- 固定列表 (Tuple)：有順序、不可變動的資料集合

	- 集合 (Set)：無順序的資料集合，ex. 水果

	- 字典：鍵值對 (Key-Value Pair) 的集合， 程式中做資料查詢 (ex. A對應到B)

- 變數 (variable)：可用來存放資料的自訂名稱，可在程式中建立名稱，未來可用自訂名稱代表資料，變數用英文，開頭不可是數字

- 字串：在程式中表達任意的文字，ex. 測試中文 是錯誤的語法，Python 語法為英文，但若想表達中文，用雙引號 (或單引號) 包起來，ex. "測試中文"、"HelloWorld"

	- 雙引號 (或單引號) 中能寫任意文字

###### <br/>
###### <br/>
###### <br/>





## 數字、字串的基本運算 <br/> 03_number-string.py

### 數字

- 基本算術運算：加 (+)、減 (-)、乘 (*)、除 (/)、取餘數 (%)

- 除法詳解：整數除法 (//)、小數除法 (/)

- X 的 Y 次方 ```X ** Y```、開根號 ```X ** 0.5```

### 字串

- 表示法詳解：雙引號 (")、單引號 (')、多行文字

- 重複 & 串接：重複相同文字或串接多個字串

- 索引 & 字元：使用索引 [] 操作字串中的字元

### 數字運算

- ```x = x + 1``` ，左邊 x 為變數，右邊 (x + 1) 要先看

- ```x = x + 1``` 可寫成 ```x += 1```

### 字串運算

```
s = "Hello"
print(s)

→

Hello
```

```
s = "Hell\"o"
print(s)

→

Hell"o
```

#### \"：跳脫

```
s = "Hello" + "World" = "Hello"  "World"
print(s)

→

HelloWorld
```

```
s = "Hello\nWorld"
print(s)

→

Hello
World
```

#### \n：跳行

```
s = """Hello
World"""
print(s)

→

Hello
World
```

##### 單雙引號皆可，前後各 3 個，中間可任意空行 (與跳行相同，兩者皆可使用)

```
s = "Hello" * 3
print(s)

→

HelloHelloHello
```

```
s = "Hello" * 3 + "World"
print(s)

→

HelloHelloHelloWorld
```

### 字串內部字元編號 (索引) 

```
s = "Hello"
print(s[0])

→

H
```

```
s = "Hello"
print(s[2])

→

l
```

##### Hello 中，H 為 0、e 為 1、l 為 2、l 為 3、o 為 4，5 沒有東西

```
s = "Hello"
print(s[1: 4])

→

ell
```

##### ※ 包含開頭，不包含結尾

###### <br/>
###### <br/>
###### <br/>





## 數字、字串的基本運算 <br/> 04_list-tuple.py

### 2 種有序列表型態：List & Tuple

- List (List 的寫法為中括號 [] )

	- 索引基本運用：取得、更新列表中的資料

	- 連續資料處理：串接、取代、連續刪除列表中的資料

	- 取得列表長度：len (列表)

	- 巢狀列表：列表中的資料也是列表

- Tuple ( Tuple 的寫法為小括號 () )

	- 資料不可更動，操作與 List 相同，但資料不可更動

### 有序可變動列表List

```
grades = [12, 60, 15, 70, 90]
print(grades)

→

[12, 60, 15, 70, 90]
```

```
grades = [12, 60, 15, 70, 90]
print(grades[0])

→

12
```

```
grades = [12, 60, 15, 70, 90]
grades[0] = 55
print(grades)

→

[55, 60, 15, 70, 90]
```

```
grades = [12, 60, 15, 70, 90]
print(grades[1: 4])

→

[60, 15, 70]
```

```
grades = [12, 60, 15, 70, 90]
# 連續刪除列表
grades[1: 4] = [] 
print(grades)

→

[12, 90]
```

```
grades = [12, 60, 15, 70, 90]
grades = grades + [12, 33]
print(grades)

→

[12, 60, 15, 70, 90, 12, 33]
```

##### 看到等號先看等號右邊

##### 可輕易做到表的串接

### 槽狀列表

```
data = [[3, 4, 5], [6, 7, 8]]
print(data[0][1])

→

4
```

##### [3, 4, 5] 為第 0 層，[6, 7, 8] 為第 1 層；3 為 0、4 為 1、5 為 2、  6 為 0、7 為 1、8 為 2

```
data=[[3, 4, 5], [6, 7, 8]]
print(data[0][0: 2])

→

[3, 4]
```

```
data = [[3, 4, 5],[6, 7, 8]]
print(data)
data[0][0: 2] = [5, 5, 5]
print(data)

→

[[3, 4, 5], [6, 7, 8]]
[[5, 5, 5, 5], [6, 7, 8]]
```

##### [3, 4, 5] 為第 0 層，[6, 7, 8] 為第 1 層；3 為 0、4 為 1、5 為 2、  6 為 0、7 為 1、8 為 2

#### Tuple 所有操作與 List 相同，但 Tuple 資料不可更動

```
data = (3, 4, 5)
data[0] = 5
print(data)

→

error
```

##### 錯誤：Tuple 的資料不可以變動

###### <br/>
###### <br/>
###### <br/>





## 集合、字典的基本運算 – Set、Dictionary <br/> 05_set-dictionary.py

### 集合

- 基本觀念：一群資料沒有順序性 (列表有順序概念，集合沒有)

- 判斷資料是否存在：使用 in 和 not in 運算符號

	- 交集、聯集：使用 & 和 | 運算符號

		- 交集：取兩個集合中相同的資料

		- 聯集：取兩個集合中的所有資料，但不重複取

	- 差集、反交集：使用 - 和 ^ 運算符號

		- 差集：從A集合中減去和B集合重疊的資料

		- 反交集：取兩個集合中不重疊的資料

- 字串拆解為集合：set (字串)

### 字典

- 基本觀念：鍵值對 (Key-value Pair)，一個索引對一個資料

- key 對應 Value：字典[Key]；字典[Key] = Value

- 判斷資料是否存在：使用 in 和 not in 運算符號

- 刪除鍵值對：使用 del 運算關鍵字

- 從列表建立字典：以列表的資料為基礎來建立字典

### 集合的運算

```
s1 = {3, 4, 5}
print(3 in s1)

→

True
```

##### 檢視 3 有無在集合內，若有為 True，若無為 False

```
s1 = {3, 4, 5}
print(10 in s1)

→

False
```

```
s1 = {3, 4, 5}
print(10 not in s1)

→

True
```

```
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 & s2
print(s3)

→

{4, 5}
```

#### 交集 (&)：取兩個集合中相同的資料

```
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 | s2
print(s3)

→

{3, 4, 5, 6, 7}
```

#### 聯集 (|)：取兩個集合中的所有資料，但不重複取

```
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 - s2
print(s3)

→

{3}
```

#### 差集 (-)：從 s1 中減去和 s2 重疊的資料

```
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 ^ s2
print(s3)

→

{3, 6, 7}
```

#### 反交集 (^)：取兩個集合中不重疊的資料

```
s = set("Hello")
print(s)

→

{'H', 'o', 'e', 'l'}
```

##### 語法為 set (字串)：集合無順序觀念，TERMINAL 顯示順序為隨機，且重複部分不會重複顯示

```
s = set("Hello")

print("H" in s)

→

True
```
```
s = set("Hello")
print("h" in s)

→

False
```

### 字典的運算：Key-value 配對

```
dic = {"apple": "蘋果", "bug": "蟲蟲"}
print(dic["apple"])

→

蘋果
```

```
dic = {"apple": "蘋果", "bug": "蟲蟲"}
dic["apple"] = "小蘋果"
print(dic["apple"])

→

小蘋果
```

```
dic = {"apple": "蘋果", "bug": "蟲蟲"}
print("apple" in dic)

→

True
```

##### 判斷對象為 key 非 value

```
dic = {"apple": "蘋果", "bug": "蟲蟲"}
print(dic)
del dic["apple"]
print(dic)

→

{'apple': '蘋果', 'bug': '蟲蟲'}
{'bug': '蟲蟲'}

```

##### 刪除字典中的鍵值對 (key-value pair)，[] 中只能選 key 不能選 value

### 從列表的資料產生字典

#### 語法：```dic = {x: x * 2 for x in [列表]}```

##### 其中 for in 固定不變

```
dic = {x: x * 2 for x in [3, 4, 5]}
print(dic)

→

{3: 6, 4: 8, 5: 10}
```

###### <br/>
###### <br/>
###### <br/>





## 流程控制：if 判斷式 <br/> 06_condition.py

> 基本語法一

```
if 布林值:
	若布林值為 True，執行命令
```

##### 前面部分為縮排 ```Tab```

> 基本語法二

```
if 布林值:
	若布林值為 True，執行命令
else:
	若布林值為 False，執行命令
```

> 基本語法三

```
if 布林值一:
	若布林值一為 True，執行命令
elif 布林值二:
	若布林值二為 True，執行命令
else:
	若布林值一和二為 False，執行命令
```

##### 布林值一是 True，代表滿足條件，滿足第一個條件跑第一段，第一個條件不滿足就看第二個條件，如果滿足第二個條件跑第二段，若第一個條件和第二個條件都是 False (都不滿足)，才跑第三段

##### elif = else if

> 程式範例

```
x = input("請輸入數字：")   # 基本輸入為字串型態
x = int(x)   # 轉換為整數型態
if x > 200:
	print("大於 200")
elif x > 100:
	print("大於 100，小於 200")
else:
	print("小於 100")
```

##### 以上為 if 語法，至 3.6 版 Python 不支援 switch 語法

##### 用 ```x = input()``` 即可在 TERMINAL 進行輸入

##### 在 TERMINAL 中 input 的數字回到程式中為字串型態，所以需用 x = int(x) 將字串型態轉換為數字型態

> 判斷式

```
if True:
	print("True 執行")
	
→

True 執行
```

```
if False:
	Print("True 執行")

→

(會直接被忽略)
```

```
if True:
	print("True 執行")
else:
	print("False 執行")

→

True 執行
```

```
if False:
	print("True 執行")
else:
	print("False 執行")

→

False 執行
```

```
x = input("請輸入數字：")
x = int(x)
if x > 100:
	print("大於 100")
else:
	print("小於等於 100")

→

請輸入數字：(在 TERMINAL 隨意輸入數字，ex. 200)
大於 100
```

```
x = input("請輸入數字：")
x = int(x)
if x > 100:
	print("大於 100")
else:
	print("小於等於 100")

→

請輸入數字：(在 TERMINAL 隨意輸入數字，ex. 50)
小於等於 100
```

```
x = input("請輸入數字：")
x = int(x)
if x > 200:
	print("大於 200")
elif x > 100:
	print("大於 100，小於等於 200")
else:
	print("小於等於 100")

→

請輸入數字：150
大於 100，小於等於 200
```

```
n1 = int(input("請輸入數字一："))
n2 = int(input("請輸入數字二："))
op = input("請輸入運算：+、-、*、/：")
if op == "+":
	print(n1 + n2)
elif op == "-":
	print(n1 - n2)
elif op == "*":
	print(n1 * n2)
elif op == "/":
	print(n1 / n2)
else:
	print("不支援的運算")

→

請輸入數字一：(在 TERMINAL 隨意輸入數字) enter
↓
請輸入數字二：(在 TERMINAL 隨意輸入數字) enter
↓
請輸入運算：+、-、*、/：(在 TERMINAL 隨意輸入 +、-、*、/ 其一) enter
↓
(自動完成上述運算)
```

##### 程式邏輯：取得第一個數字放在 n1 → 取得第二個數字放在 n2 → 最後取得 +、-、*、/ 中的其中一個放在 op → 判斷式進行判斷是否為 True，若為 True 則跑該段

###### 建議有時間自行重寫練習

###### <br/>
###### <br/>
###### <br/>





## 流程控制：迴圈基礎，while 迴圈、for 迴圈 <br/> 07_loop-basic.py

#### 迴圈：寫一段程式後不斷重複執行

> while迴圈

>> 基本語法

```
while 布林值:
	若布林值為 True，執行命令
	回到上方，做下一次的迴圈判斷
```

>>  程式範例

```
n = 1
while n < 5:
	print("變數 n 的資料是：", n)
	n += 1

→

變數 n 的資料是： 1
變數 n 的資料是： 2  
變數 n 的資料是： 3  
變數 n 的資料是： 4 
```

> for 迴圈

>> 基本語法

```
for 變數名稱 in 列表或字串:
	將列表中的項目或字串中的字元逐一取出，逐一處理
```

>> 程式範例

```
n = 1
for x in [4, 1, 2]:
	print("逐一取得列表中的資料", x)

→

逐一取得列表中的資料 4
逐一取得列表中的資料 1
逐一取得列表中的資料 2
```

```
for c in "Hello":
	print("逐一取得字串中的字元", c)

→

逐一取得字串中的字元 H
逐一取得字串中的字元 e
逐一取得字串中的字元 l
逐一取得字串中的字元 l
逐一取得字串中的字元 o
```

>> 使用 range()

#### range() 可幫忙製造連續數字的列表

```
for 變數名稱 in range(3)
相當於
for 變數名稱 in  [0, 1, 2]
```

```
for 變數名稱 in range(3, 6)
相當於
for 變數名稱 in [3, 4, 5]
```

> while 迴圈

```
n = 1
while True:
	print(n)
	n += 1

→ (此迴圈為無窮迴圈，在 TERMINAL 中 ctrl + c 即可終止)
```

```
n = 1
while n <= 3:
	print(n)
	n += 1

→
1
2
3
```

>> 1 加到 10 用 while 迴圈：

```
n = 1
sum = 0   # 紀錄累加的結果
while n <= 10:
	sum = sum + n
	n += 1
print(sum)

→

55
```

> for 迴圈

```
for x in [3, 5, 1]:
	print(x)
→
3
5
1
```

```
for x in "Hello":
	print(x)

→

H
e
l
l
o
```

```
for x in range(5):
	print(x)

→

0
1
2
3
4
```

```
for x in range(5, 10):
	print(x)

→

5
6
7
8
9
```

>> 1 加到 10 用 for 迴圈：

```
sum = 0
for x in range(1, 11):   # 因為 0 不影響加法總和，所以 range(1, 11) 可寫成 range(11)
	sum = sum + x
	print(sum)

→

55
```

###### <br/>
###### <br/>
###### <br/>





## 流程控制：迴圈進階控制，braek、continue、else 命令 <br/> 08_loop-control.py

### 迴圈搭配的指令：break 和 continue (這兩個命令一定要跟迴圈做搭配，需寫在迴圈裡面)

> break

>> 強制結束迴圈

```
while 布林值:
	break

for 變數名稱 in 列表或字串:
	break
```

>> 程式範例

```
n = 1
while n < 5:
	if n == 3:
		break
	n += 1
print(n)

→

3
```

##### 程式邏輯：當 ```n = 1```，在 ```while n < 5:``` 中為 True，但在 ```if n == 3``` 為 False，所以不會執行 ```break```，```n += 1``` 讓 ```n = 2``` 回到迴圈，當 ```n = 2```，在 ```while n < 5:``` 中為 True，但在 ```if n == 3``` 為 False 所以不會執行 ```break```，```n + =1``` 讓 ```n = 3``` 回到迴圈，當 ```n = 3```，在 ```while n < 5:``` 中為 True，在 ```if n == 3``` 也為 True，執行 ```break```，停止程式

> continue

>> 強制繼續下一圈

```
while 布林值:
	continue
for 變數名稱 in 列表或字串:
	continue
```

>> 程式範例

```
n = 0
for x in [0, 1, 2, 3]:
	if x % 2 == 0:
		continue
	n += 1
print(n)

→

2
```

##### %：取餘數，mode；```x % 2 == 0``` 表示 x 被 2 整除

##### 程式邏輯：當 ```n = 0```，```x = 0``` 進入 ```if x % 2 == 0``` 為 True，執行 continue 進入下一圈 (忽略下方 (n += 1) 程式碼)，```x = 1``` 進入 ```if x % 2 == 0``` 為 False，不會執行 continue，```n += 1``` 讓 ```n = 1```，```x = 2``` 進入 ```if x % 2 == 0``` 為 True，執行 continue 進入下一圈，```x = 3``` 進入 ```if x % 2 == 0 為 False```，```n += 1``` 讓 ```n = 2```

##### 原本 ```n += 1``` 要執行 4 次，但因 continue 所以只執行 2 次

### 迴圈結構在最後面可以加 else 的語法

> else

>> 基本語法

```
while 布林值:
	若布林值為 True，執行命令
	回到上方，做下一次的迴圈判斷
else:
	迴圈結束前，執行此區塊的命令
```

```
for 變數名稱 in 列表或字串:
	將列表中的項目或字串中的字元逐一取出，逐一處理
else:
	迴圈結束前，執行此區塊的命令
```

>> 程式範例

```
n = 1
while n < 5:
	print("變數 n 的資料是：", n)
	n += 1
else:
	print(n)

→

5
```

```
for c in "Hello":
	print("逐一取得字串中的字元", c)
else:
	print(c)

→

o
```

### break 的簡易範例

```
n = 0
while n < 5:
	if n == 3:
		break
		print(n)   # 印出迴圈中的 n
	n += 1
print("最後的 n：", n)   # 印出迴圈結束後的 n

→

0
1
2
最後的 n： 3
```

###### crtl + 右邊 shift 旁的 / 可以直接進行註解

### continue 的簡易範例

```
n = 0
for x in [0, 1, 2, 3]:
	if x % 2 == 0:   # x 是偶數 %：取餘數
		continue
	print(x)
	n += 1
print("最後的 n：", n)

→

1
3
最後的 n： 2
```

### else 的簡易範例

```
sum = 0
for n in range(11):
	sum += n
else:
	print(sum)   # 印出 0 + 1 + 2 + 3 + ... + 10 的結果

→

55
```

### 綜合範例：找出整數平方根

#### 輸入 9，得到 3；輸入 11 得到 "沒有整數的平方根"：

```
n = input("輸入一個正整數：")
n = int(n)   # 轉換輸入成數字
for i in range(n):   # i 從 0 ~ n - 1
	if i * i == n:
	print("整數平方根", i)
	break   # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
	print("沒有整數的平方根")

→

輸入一個正整數：25 enter
整數平方根 5
```

```
n = input("輸入一個正整數：")
n = int(n)   # 轉換輸入成數字
for i in range(n):   # i 從 0 ~ n - 1
	if i * i == n:
	print("整數平方根", i)
	break   # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
	print("沒有整數的平方根")

→

輸入一個正整數：12 enter
沒有整數平方根
```

###### <br/>
###### <br/>
###### <br/>





## 函式基礎：定義並呼叫函式 <br/> 09_function-basic.py

> 函式

#### 程式區塊 (函式：程式碼包裝在一個區塊中，方便隨時呼叫，函式就是一個程式區塊)

#### 定義 > 呼叫：要先定義 (建立) 函式，然後才能呼叫 (使用) 函式

> 定義函式

>>基本語法

```
def 函式名稱(參數名稱):
	函式內部的程式碼
```

##### def 代表 define

>> 程式範例：定義一個印出 Hello 的函式

```
def sayHello():
	print("Hello")
```

##### sayHello 名字自取，但不可是中文及數字，只能是一般的英文

>> 程式範例：定義可以印出任何訊息的函式

```
def say(msg):
	print(msg)
```

##### 想法：把參數內的資料 ( () 內的資料) 印出來，暫時還不知道資料為何，只是先定義名字 (變數的概念)

>> 程式範例：定義一個可以做加法的函式

```
def add(n1, n2):
	result = n1 + n2
	print(result)
```

> 呼叫函式

>> 基本語法
```
函式名稱(變數資料)
```

>> 程式範例：定義一個印出 Hello 的函式

```
def sayHello():
	print("Hello")
sayHello()   # 呼叫上方定義的函式
```

##### 呼叫函式：跳到函式裡面

>> 程式範例：定義可以印出任何訊息的函式

```
def say(msg):
	print(msg)
say("Hello Function")   # 呼叫上方定義的函式
say("Hello Python")   # 呼叫上方定義的函式
```

##### 函式參數的設計在呼叫時有彈性

>> 程式範例：定義一個可以做加法的函式

```
def add(n1, n2):
	result = n1 + n2
	print(result)
# 呼叫上方定義的函式
add(3, 4)
add(7, 8)
```

> 回傳值

>> 基本語法

```
def 函式名稱(參數名稱):
	函式內部的程式碼
	return   # 結束函式，回傳None
```

##### 程式內寫下 return，代表程式強制結束

##### 資料：數字、字串、布林值、列表、字典、物件 …

>> 程式範例：函式回傳 None

```
def say(msg):
	print(msg)
	return
# 呼叫函式，取得回傳值
value = say("Hello Function")
print(value)

→

None
```

##### 函式呼叫的結果，就是回傳值，也就是 None (say("Hello Function"))，None 放進變數 value，印出 value，印出 None

>> 程式範例：函式回傳字串 Hello

```
def add(n1, n2):
	result = n1 + n2
	return "Hello"
# 呼叫函式，取得回傳值
value = add(3, 4)
print(value)

→

Hello
```

##### 程式邏輯：呼叫 add，3 放進 n1，4 放進 n2，3 + 4 = 7 放進 result，return 字串 Hello，字串Hello 被丟回 add(3, 4)，add(3, 4) 為字串 Hello = value，印出 value

##### result的7沒有用，因為return的是Hello

##### 最後函式呼叫完得到的要看回傳值 (return)，和程式碼無關

>> 函式內部的程式碼，若是沒有做函式呼叫，就不會執行

```
def multiply():
	print(3 * 4)

→

無錯誤但不執行
```

##### 函式內部的 code (程式碼)，沒有呼叫就不會執行

```
def multiply():
	print(3 * 4)
multiply()

→

12
```

```
def multiply():
	print(3 * 4)
multiply()
multiply()

→

12
12
```

>> 透過參數得到彈性

```
def multiply(n1, n2):
	print(n1 * n2)
multiply(3, 4)
multiply(10, 8)

→

12
80
```

```
def  multiply(n1, n2):
	print(n1 * n2)
value=multiply(3, 4)
print(value)

→

12
None
```

```
def multiply(n1, n2):
	print(n1 * n2)
	return
value = multiply(3, 4)
print(value)

→

12
None
```

##### return後面沒有帶回傳值就跟沒寫一樣

```
def multiply(n1, n2):
	print(n1 * n2)
	return 10
value = multiply(3, 4)
print(value)

→

12
10
```

```
def  multiply(n1, n2):
	print(n1 * n2)
	return n1 * n2
value = multiply(3, 4)
print(value)

→

12
12
```

##### 可以直接在裡面印出來，也可以回傳到外面印出來

```
def multiply(n1, n2):
	return n1 * n2
value = multiply(3, 4)
print(value)

→

12
```

```
def multiply(n1, n2):
	print(n1 * n2)
	return n1 * n2
value = multiply(3, 4)

→

12
```

>> 回傳值的好處是可以在外部繼續操作

```
def multiply(n1, n2):
	return n1 * n2
value = multiply(3, 4) + multiply(10, 5)   # (3 * 4) + (10 * 5)
print(value)

→

62
```

> 程式的包裝

>> 同樣的邏輯可以重複利用

```
sum = 0
for n in range(1, 11):
	sum = sum + n
print(sum)

sum = 0
for n in range(1, 21):
	sum = sum + n
print(sum)

→

55
210
```

#### 類似的工作一直做 (copy test)，就會做程式的包裝

##### 函式最大的用途就是做程式的包裝

```
def calculate(max):
	sum = 0
	for n in range(1, max + 1):
		sum = sum + n
	print(sum)
calculate(10)
calculate(20)

→

55
210
```

###### <br/>
###### <br/>
###### <br/>





## 函式參數詳解：參數預設值、名稱對應、任意長度參數 (函式進階) <br/> 10_function-args.py

>預設資料

>> 基本語法

```
def 函式名稱(參數名稱 = 預設資料):
	函式內部的程式碼
```

>> 程式範例

```
# 參數 msg 預設資料為 "Hello"
def say(msg = "Hello"):
	print(msg)
# 印出 Hello Function
	say("Hello Function")
say()   # 印出預設資料Hello
```

##### 用 say("Hello Function") 會印出 Hello Function，但用 say() 因 () 無資料所以會採用預設資料

> 名稱對應

>> 基本語法

```
def 函式名稱(名稱1, 名稱2):
	函式內部的程式碼
# 呼叫函式，以參數名稱對應資料
函式名稱(名稱2 = 3, 名稱1 = 5)
```

##### 呼叫函式名稱式可以倒過來，重點是前面要加參數名稱

>> 程式範例

```
# 定義一個可以做除法的函數
def divide(n1, n2):
	result = n1 / n2
	print(result)
divide(2, 4)   # 印出 0.5
divide(n2 = 2, n1 = 4)   # 印出 2.0
```

> 無限參數

>> 基本語法

```
def 函式名稱(*無限參數):
	無限參數以 Tuple 資料型態處理函式內部的程式碼
# 呼叫程式，可傳入無限數量的參數
函式名稱(資料一, 資料二, 資料三)
```

##### 呼叫函式中可以放不定量的資料

>> 程式範例

```
# 函式接受無限參數 msgs
def say(*msgs):
	#以Tuple的方式處理
	for msg in msgs
		print(msg)
# 呼叫函式，傳入三個參數資料
say("Hello", "Arbitrary", "Arguments")
```

##### 若給 3 個字串，就會變成 3 個字串的 Tuple，用一個迴圈將 Tuple 資料取出

#### Tuple：有序列表(資料不可更動)，List 資料可更動

#### 參數的預設資料

```
def power(base, exp = 0):
	print(base ** exp)
power(3, 2)
power(4)

→

9
1
```

##### power(4) 因為沒有給次方數，因此帶入預設值 0

>> 使用參數對應名稱

```
def divide(n1, n2):
	print(n1 / n2)
divide(2, 4)
divide(n2 = 2, n1 = 4)

→

0.5
2.0
```

>> 無限 / 不定 參數資料

```
def avg(*ns):
	print(ns)
avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)

→

(3, 4)
(3, 5, 10)
(1, 4, -1, -8)
```

##### 參數的資料會變成 Tuple 的形態傳遞進去

```
def avg(*ns):
	for n in ns:
		print(n)
avg(3, 4)

→

3
4
```

```
def avg(*ns):
	sum = 0
	for n in ns:
		sum = sum + n
		print(sum / len(ns))
avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)

→

3.5
6.0
-1.0
```

##### len：列表 (Tuple) 的長度

###### <br/>
###### <br/>
###### <br/>





## Module 模組的載入與使用 <br/> 11_module.py

### Python 中所謂的模組，就是獨立的程式檔案，可以被其他的程式載入和使用，其中最大的好處是可以重複使用，在程式碼太長太多時可以寫成不同的檔案模組重複使用，這就是 Python 的模組要解決的問題

### 模組(module)

- 獨立的程式檔案：將程式寫在一個檔案中，此檔案可重複載入使用 

- 載入 > 使用：先載入模組，再使用模組中的函式或變數

> 載入模組

>> 基本語法

```
import 模組名稱
```

```
import 模組名稱 as 模組別名
```

> 使用模組

>> 基本語法

```
模組名稱或別名.函式名稱(參數資料)
```

```
模組名稱或別名.變數名稱
```

> 內建模組 (Python 語言中已內建好的模組)

#### sys 模組：取得系統相關資料

>> 程式範例

```
# 載入sys模組
import sys

# 使用 sys 模組
print(sys.platform)   # 印出作業系統
print(sys.maxsize)   # 印出整數型態的最大值
print(sys.path)   # 印出搜尋模組的路徑
```

```
# 載入sys模組 
import sys as s

# 使用 sys 模組
print(s.platform)   # 印出作業系統
print(s.maxsize)   # 印出整數型態的最大值
print(s.path)   # 印出搜尋模組的路徑

※ s 是別名
```

> 自訂模組

#### 建立幾何運算模組：建立檔案 geometry.py，定義平面幾何運算用的函式

##### 載入與使用：載入 geometry 模組，並使用模組中定義的功能

```
import sys

print(sys.platform)
print(sys.maxsize)

→ 

win32
9223372036854775807
```

```
import sys as system

print(system.platform)
print(system.maxsize)

→

win32
9223372036854775807
```

#### 建立 geometry 模組，載入使用(自訂模組)

##### 先另開一個 python 檔案命名 geometry.py，並在其中自訂模組

```
# 在 geometry 模組中定義幾何運算功能

# 計算兩個點的距離
def distance(x1, y1, x2, y2):
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 計算線段的斜率
def slope(x1, y1, x2, y2):
	return (y2 - y1) / (x2 - x1)
```

##### 回到主程式 (11_module.py)

```
import geometry

result=geometry.distance(1, 1, 5, 5)
print(result)
result=geometry.slope(1, 2, 5, 6)
print(result)

→ 

5.656854249492381
1.0
```

##### 調整搜尋模組的路徑

```
import sys

print(sys.path)   # 印出模組的搜尋路徑列表

→ 

['D:\\Python-training','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\DLLs','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\lib','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
```

##### 在資料夾中建立一個資料夾 (modules)，將 11_module.py 移入

```
import sys
import geometry

print(geometry.distance(1, 1, 5, 5))

→ 

Traceback (most recent call last):
  File "D:\Python-training\11_module.py", line 16, in <module>
	import geometry
ModuleNotFoundError: No module named 'geometry'
```

##### 在模組的搜尋路徑中，並沒有包含自己創建的資料夾(modules)，因此產生錯誤 

```
import sys

sys.path.append("modules")   # 在模組的搜尋路徑列表中[新增路徑]
print(sys.path)   # 印出模組的搜尋路徑列表
print("=========================================")

import geometry
print(geometry.distance(1, 1, 5, 5))

→ 

['D:\\Python-training','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\DLLs','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\lib','C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\charmy\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 'modules']

=========================================

5.656854249492381
```

##### 路徑的最後多了 'modules'

###### <br/>
###### <br/>
###### <br/>





## Package 封包的設計與使用 <br/> 12_main.py

### 封包：包含模組的資料夾(用來整理、分類模組程式)

- 檔案系統中的資料夾對應到Python的封包

- 檔案系統中的檔案對應到模組

> 建立封包

>> 專案檔案配置

```
- 專案資料夾
	- 主程式.py
	- 封包資料夾
		- __init__.py
		- 模組一.py
		- 模組二.py

# 有裝- __init__.py的資料夾才會被當作封包，若無- __init__.py則為普通資料夾，- __init__.py裡面留空即可，但檔案要建立，__為兩個底線
```

>> 專案檔案配置範例

```
- 專案資料夾
	- main.py
	- geometry
		- __init__.py
		- point.py
		- line.py
```

> 使用封包

>> 基本語法

```
import 封包名稱.模組名稱
```

```
import 封包名稱.模組名稱 as 模組別名
```

1. 新增資料夾 (backup)，將先前程式移入其中

2. 把程式放進 backup 後，要改寫成 python backup\檔案名.py 或先輸入 cd backup(資料夾名) 後輸入檔案名才能執行

3. 新增封包並在其中建立檔案 ```__init__.py```、```point.py```、```line.py ```

#### point.py

```
def distance(x, y):
	return (x ** 2 + y ** 2) ** 0.5
```

#### line.py

```
def len(x1, y1, x2, y2):
	return ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ** 0.5
def slope(x1, y1, x2, y2):
	return (y2 - y1) / (x2 - x1)
```

#### main.py

```
import geometry.point
result = geometry.point.distance(3, 4)
print("距離", result)

import geometry.line
result = geometry.line.slope(1, 1, 3, 3)
print("斜率", result)

→ 

距離 5.0
斜率 1.0
```

##### geometry.point為模組的完整名稱

#### 若覺得封包名稱太長，可以使用別名

```
import geometry.point as point
result = point.distance(3, 4) 
print("距離", result) 

import geometry.line as line 
result = line.slope(1, 1, 3, 3) 
print("斜率", result) 

→ 

距離 5.0
斜率 1.0
```

###### <br/>
###### <br/>
###### <br/>





## 文字檔案的讀取和儲存 <br/> 13_file.py

### 檔案操作流程 ：開啟檔案 > 讀取或寫入 > 關閉檔案

> 開啟檔案

>> 基本語法

```
檔案物件 = open(檔案路徑, mode = 開啟模式)
```

- 開啟模式

- 讀取模式 - r

- 寫入模式(儲存) - w

-讀寫模式 – r+

> 讀取檔案

>> 讀取全部文字 

```
檔案物件.read()
```

>> 一次讀取一行 

```
for 變數 in 檔案物件:
	從檔案依序讀取每行文字到變數中
```

>> 讀取 JSON 格式

```
import json

讀取到的資料 = json.load(檔案物件)
```

- 資料格式 JSON 使用的非常頻繁，經常用於網路中交換資料或儲存設定檔

> 寫入檔案(儲存檔案) # 因為英文是 write 所以有翻譯問題

>> 寫入文字

```
檔案物件.write("字串")
```

>> 寫入換行符號

```
檔案物件.write("這是範例文字\n") 
```

>> 寫入 JSON 格式

```
import json

json.dump(要寫入的資料, 檔案物件)
```

> 關閉檔案

>> 基本語法

```
檔案物件.close()
```

> 最佳實務

```
with open(檔案路徑, mode = 開啟模式) as 檔案物件:
	讀取或寫入檔案的程式

# 以上區塊會自動、安全的關閉檔案
```

>> 儲存檔案

```
file = open("data.txt", mode="w")   # 開啟 
file.write("Hello File")   # 操作 
file.close()   # 關閉 

→

產生新的檔案data.txt在資料夾裡 
data.txt → 
Hello File 
```

#### 同一個檔案打開再重新寫入會有覆蓋的效果(檔案的內容會被整個覆蓋)，即用新的資料覆蓋檔案裡的內容 

```
file = open("data.txt", mode = "w")
file.write("Hello File\nSecond Line")
file.close()

→

data.txt →
Hello File
Second Line
```

```
file = open("data.txt", mode = "w")
file.write("測試中文\n好棒棒")
file.close()

→

data.txt →
���դ���
�n�δ�
# 出現亂碼
```

#### 若要顯示中文，需要先指定utf-8編碼(最常見的)

```
file = open("data.txt", mode = "w",encoding = "utf-8")
file.write("測試中文\n好棒棒")
file.close()

→

data.txt →
測試中文
好棒棒
```

> 最佳實務寫法

```
with open("data.txt", mode = "w", encoding = "utf-8") as file:
	file.write("測試中文\n好棒棒")

→

data.txt → 
測試中文
好棒棒
```

##### 不需要寫 close，會自動、安全、可靠的將檔案資源釋放、關閉

>> 讀取檔案(讀取已經存在的檔案)


- 寫入：不存在沒關係，可以創造新檔案 

```
with open("data.txt", mode = "r", encoding = "utf-8") as file:
	data = file.read()

print(data)

→

測試中文
好棒棒
```
#### 寫入數字檔案後讀取且把每行數字做加法

```
# 儲存檔案
with open("data.txt", mode = "w", encoding = "utf-8") as file:
	file.write("5\n3")

# 讀取檔案
# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
sum = 0
with open("data.txt", mode = "r", encoding = "utf-8") as file:
	for line in file:   # 一行一行讀取
		sum+=int(line)
print(sum)

→

8
```

##### 儲存檔案中先產生新的檔案 data.txt 在資料夾裡並將 5 和 3 在不同行顯示，在讀取檔案中將 data.txt 的 5 和 3 讀取並相加

> 使用 JSON 讀取格式、複寫檔案

#### 新增檔案 config.json

```
{
	"name":"My Name",
	"version":"1,2,5"
}
```

#### file.py

```
import json
with open("config.json", mode = "r") as file:
	data = json.load(file)

print(data)   # 是一個字典資料
print("name：", data["name"])
print("version：", data["version"])

→ 

name： My Name

version： 1,2,5
```

>> 修改資料

#### config.json

```
{
	"name":"My Name",
	"version":"1,2,5"
}
```

#### file.py

```
# 從檔案中讀取JSON資料，放入變數data裡面
with open("config.json", mode = "r") as file:
	data = json.load(file)

print(data)   # 是一個字典資料

data["name"] = "New Name"   # 修改變數中的資料

# 把最新的資料複寫回檔案中
with open("config.json", mode = "w") as file:
	json.dump(data,file)

→

{'name': 'New Name', 'version': '1,2,5'}
```

###### <br/>
###### <br/>
###### <br/>





## 亂數與統計模組 <br/> 14_file.py

### 內建模組：學習 random 和 statistics 模組 

> 亂數模組

>> 載入模組

```
import random
```

>> 隨機選取

```
import random

# 從列表中隨機選取1個資料 
random.choice([0, 1, 5, 8]) 

# 從列表中隨機選取2個資料 
random.sample([0, 1, 5, 8], 2) 
```

##### 若想選取 3 個資料，把 2 改成 3；選取資料數不能超過列表長度

>> 隨機調換順序

```
import random

# 將列表的資料「就地」隨機調換順序
data = [0, 1, 5, 8]
random.shuffle(data)

print(data)
```

##### 就地：將 data 本身進行修改

>> 隨機亂數

```
import random

# 取得 0.0 ~ 1.0 之間的隨機亂數
random.random()
random.uniform(0.0, 1.0)
```

##### uniform：機率相同

>> 常態分配亂數

```
import random 

# 取得平均數 100、標準差 10 的常態分配亂數 
random.normalvariate(100, 10) 
```

###### <br/>

![](./MarkDown-img/normalDistribution.jpg)

###### <br/>

> 統計模組

>> 載入模組

```
import statistics
```

>> 使用模組

```
import statistics

# 計算列表中數字的平均數
statistics.mean([1, 4, 6, 9]) 

# 計算列表中數字的中位數
statistics.median([1, 4, 6, 9])

# 計算列表中數字的標準差   
statistics.stdev([1, 4, 6, 9])
```

##### 標準差：代表資料散佈的狀況 

> 隨機模組

#### 隨機選取：TERMINAL 每次出現的數字都不同

```
import random

data = random.choice([1, 5, 6, 10, 20])
print(data)

→

10
```

```
import random

data=random.sample([1, 5, 6, 10, 20], 3)
print(data)

→

[1, 20, 6]
```

#### 隨機調換順序：隨機直接調換 data 本身順序，TERMINAL每次出現的順序都不同

```
import random

data=[1, 5, 8, 20]
random.shuffle(data)
print(data)

→

[8, 20, 1, 5]
```

#### 隨機選取亂數：TERMINAL 每次出現的數字都不同

```
import random

data = random.random()   # 0.0 ~ 1.0 之間的隨機亂數
print(data)

→

0.09932831340192749
```

##### 等於

```
import random

data = random.uniform(0.0, 1.0)   # 0.0 ~ 1.0 之間的隨機亂數
print(data)

→

0.7038663863717032
```

```
import random

data = random.uniform(60, 100)   # 60 ~ 100 之間的隨機亂數
print(data)

→

64.21584558160195
```

#### 取得常態分配亂數

```
# 平均數100，標準差10，得到的資料多數在 90 ~ 110 之間

data = random.normalvariate(100, 10)
print(data)

→

112.49345426404079
```

```
# 平均數 0，標準差 5，得到的資料多數在 -5 ~ 5 之間

data = random.normalvariate(0, 5)
print(data)

→

7.198595824699282
```

> 統計模組 

```
import statistics as stat

data = stat.mean([1, 4, 5, 8])
print(data)

→

4.5
```

```
import statistics as stat

data = stat.mean([1, 2, 3, 4, 5, 8, 100])
print(data)

→

17.571428571428573
```

```
import statistics as stat

# 中位數不會被極端值影響
data = stat.median([1, 2, 3, 4, 5, 8, 100])
print(data)

→

4
```

```
import statistics as stat

data = stat.stdev([1, 2, 3, 4, 5, 8, 100])
print(data)

→

36.41820580816296
```

```
import statistics as stat

data = stat.stdev([1, 2, 3, 4, 5, 8, 10])
print(data)

→ 

3.251373336211726
```