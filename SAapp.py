#! /usr/bin/env python3

from ast import Delete
import cgi
import sqlite3

db_path = "bookdb.db"           # データベースファイル名を指定

con = sqlite3.connect(db_path)  # データベースに接続
con.row_factory = sqlite3.Row   # 属性名で値を取り出せるようにする
cur = con.cursor()              # カーソルを取得


form = cgi.FieldStorage()
param_str = form.getvalue('param1', '')
try:
    # SQL文の実行
    title = param_str
    author = param_str
    cur.execute("select * from BOOKLIST where TITLE like ? or AUTHOR like ?", ('%' + title + '%', '%' + author + '%'))
    rows = cur.fetchall()
    if not rows:                # リストが空のとき
        print("Content-type: text/html")
        print("")
        print("<html>")
        print("<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
        print("<body>")
        print("そんな本はありません")
        print(" </body>")
        print("</html>")
    else:
        print("Content-type: text/html")
        print("")
        print("<html>")
        print("<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
        print("<body>")
        print("<h1>'%s'の検索結果</h1>" % str(param_str))
        print("ISBNを入力してください")
        print("""<table border="1">""")
        print("  <form name=\"form1\" action=\"/cgi-bin/insert.py\" method=\"POST\">")
        print("<tr>")
        print("<th>ID</th>")
        print("<th>タイトル</th>")
        print("<th>著者</th>")
        print("<th>出版社</th>")
        print("<th>価格</th>")
        print("<th>ISBN</th>")
        print("<th>追加</th>")
        print("</tr>")
        print("<tr>")
        print("<th>")
        print("        <input type=\"text\" name=\"info1\" />")
        print("</th>")
        print("<th>")
        print("        <input type=\"text\" name=\"info2\" />")
        print("</th>")
        print("<th>")
        print("        <input type=\"text\" name=\"info3\" />")
        print("</th>")
        print("<th>")
        print("        <input type=\"text\" name=\"info4\" />")
        print("</th>")
        print("<th>")
        print("        <input type=\"text\" name=\"info5\" />")
        print("</th>")
        print("<th>")
        print("        <input type=\"text\" name=\"info6\" />")
        print("</th>")
        print("<th>")
        print("        <button type=\"submit\" name=\"submit\" onclick=\"return check();\">追加する</button>")
        print("  </form>")
        print("</th>")
        print("</tr>")
        print("</table>")
        
        print("""<table border="2">""")
        print("<tr>")
        print("<th>ID</th>")
        print("<th>タイトル</th>")
        print("<th>著者</th>")
        print("<th>出版社</th>")
        print("<th>価格</th>")
        print("<th>ISBN</th>")
        print("<th>削除</th>")
        print("</tr>")
        for row in rows:
            print("<tr>")
            print("<td>%d</td>" % row['ID'])
            print("<td>%s</td>" % str(row['TITLE']))
            print("<td>%s</td>" % str(row['AUTHOR']))
            print("<td>%s</td>" % str(row['PUBLISHER']))
            print("<td>%d</td>" % row['PRICE'])
            print("<td>%s</td>" % str(row['ISBN']))
            print("<td>")
            print("		<form action=\"delete.py\" method=\"post\">")
            print("		<input type=\"submit\" value=\"削除する\">")
            print("		<input type=\"hidden\" name=\"param2\" value=%s>" % str(row['ISBN']))
            print("  </form>")
            print("</td>")
            print("</tr>")
        print("</table>")
        print("</body>")
        print("</html>")


except sqlite3.Error as e:      # エラー処理
    print("Error occurred:", e.args[0])

con.commit()
con.close()