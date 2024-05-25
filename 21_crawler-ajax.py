# 抓取 PTT 電影版的網頁原始碼(HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"



# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url,headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")



# 解析原始碼，取得每天文章標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser") # 讓BeautifulSoup協助解析HTML格式文件
titles = root.find_all("div", class_ = "title") # 尋找所有class="title"的div標籤
for title in titles:
    if title.a != None:   #如標題包含 a 標籤(沒有被刪除)，印出來
        print(title.a.string)

# Medium無法已經重新包裝！