#! /usr/bin/env python3
from ast import Delete
import cgi
import sqlite3
from traceback import print_exception
from turtle import pensize

db_path = "bookdb.db"           # データベースファイル名を指定

con = sqlite3.connect(db_path)  # データベースに接続
con.row_factory = sqlite3.Row   # 属性名で値を取り出せるようにする
cur = con.cursor()              # カーソルを取得


form = cgi.FieldStorage()
id = form.getvalue('info1', '')
title = form.getvalue('info3', '')
author = form.getvalue('info2', '')
publisher = form.getvalue('info4', '')
price = form.getvalue('info5', '')
isbn = form.getvalue('info6', '')

try:
    cur.execute("INSERT INTO BOOKLIST values (?,?,?,?,?,?);", (id, title, author, publisher, price, isbn, ))
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("  <head>")
    print("    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>")
    print("  </head>")
    print(" <body>")
    print("""<table border="2">""")
    print("<tr>")
    print("<th>ID</th>")
    print("<th>タイトル</th>")
    print("<th>著者</th>")
    print("<th>出版社</th>")
    print("<th>価格</th>")
    print("<th>ISBN</th>")
    print("</tr>")
    print("<tr>")
    print("<th>")
    print(id)
    print("</th>")
    print("<th>")
    print(title)
    print("</th>")
    print("<th>")
    print(author)
    print("</th>")
    print("<th>")
    print(publisher)
    print("</th>")
    print("<th>")
    print(price)
    print("</th>")
    print("<th>")
    print(isbn)
    print("</th>")
    print("</tr>")
    print("</table>")
    print("を追加しました")
    print(" <body>")
    print("  <form name=\"form1\" action=\"SAapp.py\" method=\"POST\">")
    print("        <input type=\"text\" name=\"param1\" />")
    print("        <button type=\"submit\" name=\"submit\" onclick=\"return check();\">submit</button>")
    print("  </form>")
    print(" </body>")
    print("</html>")

except sqlite3.Error as e:      # エラー処理
    print("Error occurred:", e.args[0])

con.commit()
con.close()