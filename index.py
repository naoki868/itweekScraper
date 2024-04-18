from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverの設定
service = Service(executable_path=ChromeDriverManager().install())

# SeleniumのWebDriverオブジェクトを生成
driver = webdriver.Chrome(service=service)

# URLを開く
driver.get('https://www.japan-it.jp/spring/ja-jp/search/2024/directory.html?locale=ja-JP&query=&refinementList%5B0%5D%5B0%5D=filters.%E8%A3%BD%E5%93%81%2F%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9.lvl0%3Aid-798786&refinementList%5B0%5D%5B1%5D=sponsoredCategory.id%3A798788&refinementList%5B0%5D%5B2%5D=sponsoredCategory.id%3A798793&refinementList%5B1%5D%5B0%5D=sponsoredCategory.id%3A798788&refinementList%5B1%5D%5B1%5D=sponsoredCategory.id%3A798793&refinementList%5B1%5D%5B2%5D=sponsoredCategory.id%3A798788&refinementList%5B1%5D%5B3%5D=filters.%E8%A3%BD%E5%93%81%2F%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9.lvl1%3Aid-798788&refinementList%5B1%5D%5B4%5D=filters.%E8%A3%BD%E5%93%81%2F%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9.lvl1%3Aid-798793#/')

# JavaScriptがロードされるのを待つ
time.sleep(20)  # 適宜調整すること

# HTMLを取得
html = driver.page_source


# BeautifulSoupで解析
soup = BeautifulSoup(html, 'html.parser')

# with open('company_names_htmlparse.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(soup)

# 'company-info'クラスを持つdivタグを全て抽出
company_info_divs = soup.find_all('div', class_='company-info')

# CSVファイルに保存
with open('company_names.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name'])  # CSVのヘッダー部分

    for div in company_info_divs:
        company_name = div.find('h3')
        if company_name:
            writer.writerow([company_name.text])  # 会社名をCSVに書き出す

# ブラウザを閉じる
driver.quit()
