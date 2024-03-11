# ------------------------------------------------------------------------------
# BeautifulSoup
#   Project Site: https://www.crummy.com/software/BeautifulSoup/
#   Document    : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# ------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import re
import requests

# ------------------------------------------------------------------------------
# Test Content
# ------------------------------------------------------------------------------
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This is a paragraph of text.</p>
    <ul>
        <li id="list_1" class="class_1">List item one</li>
        <li id="list_2" class="class_2">List item two</li>
        <li id="list_3" class="class_3">List item three</li>
    </ul>
    <custom>
      <a href="http://www.example1.com">Visit Example1</a>
      <a href="http://www.example2.com">Visit Example2</a>
      <a href="http://www.example3.com">Visit Example3</a>
    </custom>
</body>
</html>
"""

# ------------------------------------------------------------------------------
# Use BeautifulSoup
# ------------------------------------------------------------------------------
soup = BeautifulSoup(html_content, 'html.parser')

# - - - - - - - - - - - - - - - - - - -
# Beautiful Soup オブジェクト
# - - - - - - - - - - - - - - - - - - -
# 全データ出力
print(soup, "\n")

# タグを除いてデータ出力
print(soup.get_text(), "\n")
# NOTE: 同義 => print(soup.text, "\n")

# stripped_stringsを使った場合。
for string in soup.stripped_strings :
    print(string)
print()

# 各DOMについて出力
print(soup.title)             # DOM
print(soup.title.name)        # HTML TagName
print(soup.title.string)      # HTML Content
print(soup.ul.text)           # HTML Content Recursive
print(soup.title.parent.name) # Parent TagName
print()

print(soup.p)
print(soup.ul)
print(soup.li.text) # NOTE: 属性が複数ある場合、最初にあるものを取得する
print()

# Domのプロパティを取得する
print(soup.li['id'])
print(soup.li['class'])
print(soup.li.attrs) # 全プロパティ
print()

# - - - - - - - - - - - - - - - - - - -
# 検索方法
# - - - - - - - - - - - - - - - - - - -
# findメソッド => 該当する要素を検索
print(soup.find('a'))
print(soup.find('li', id='list_3'))
print()

# find_all => 該当する要素全てを配列で取得
print(soup.find_all('li'))
print(soup.find_all(['li', 'a'])) # or 検索
print(soup.find_all(string="List item one"))                    # キーワード検索 (単数)
print(soup.find_all(string=["List item one", "List item two"])) # キーワード検索 (複数)
print(soup.find_all(string=re.compile("List")))                 # キーワード検索 (正規表現)
print()

# find_allの結果を走査して特定のプロパティを出力
for link in soup.find_all('a'):
  print(link.get('href'))
print()

# 正規表現
for tag in soup.find_all(re.compile("^custom$")):
    print(tag.name)
print()

# - - - - - - - - - - - - - - - - - - -
# 子要素の取得
# - - - - - - - - - - - - - - - - - - -
# contentsメソッド
print(soup.ul.contents)
print(soup.ul.contents[3].string)

# childrenメソッド => 子要素をイテレータとして取得
for child in soup.custom.children:
    print(child)

# descendantsメソッド
# => 子要素をイテレータとして再帰的に取得
for descendant in soup.custom.descendants:
    print(descendant)

# ------------------------------------------------------------------------------
# HTMLを読み込んで処理する
# ------------------------------------------------------------------------------
# Get Response Data
url      = "https://www.crummy.com/software/BeautifulSoup/bs4/doc"
response = requests.get(url)
html     = response.text
soup     = BeautifulSoup(html, 'html.parser')

for h1_dom in soup.find_all("h1"):
    print(h1_dom.text)
