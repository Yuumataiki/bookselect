#! /usr/bin/env python3
from ast import Delete
import cgi
import sqlite3

db_path = "bookdb.db"           # データベースファイル名を指定

con = sqlite3.connect(db_path)  # データベースに接続
con.row_factory = sqlite3.Row   # 属性名で値を取り出せるようにする
cur = con.cursor()              # カーソルを取得


form = cgi.FieldStorage()
isbn = form.getvalue('param2', '')

try:
    cur.execute("DELETE FROM BOOKLIST where ISBN = ?", (isbn,))
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("  <head>")
    print("    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>")
    print("  </head>")
    print(" <body>")
    print(isbn)
    print("を削除しました")
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