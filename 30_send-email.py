# 寄送 Email 的程式

# 準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "要寄送的信箱"
msg["To"] = "接受信的信箱"
msg["Subject"] = "酷啦皮卡丘"



# 寄送純文字的內容
msg.set_content("測試")



# 寄送比較多樣式的內容(html)
msg.add_alternative("<p>HTML內容</p>進行測試", subtype = "html")



# 連線到 SMTP Server，驗證寄件人身份並發送郵件
import smtplib



# 到網路上查詢 gmail smtp server 或是 yahoo smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("要寄送的信箱", "要寄送的信箱密碼")
server.send_message(msg)
server.close()