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