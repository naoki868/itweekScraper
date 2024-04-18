import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import csv

# CSVファイルを読み込む
df = pd.read_csv('companies.csv')
company_names = df['Company Name'].tolist()

# Selenium設定
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 結果を保存するためのCSVファイルを開く
with open('company_details.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'URL', 'Summary'])  # ヘッダー

    # 30行ずつ処理
    for i in range(0, len(company_names), 30):
        # 各会社について処理
        for name in company_names[i:i+30]:
            # Googleで会社名を検索
            driver.get(f'https://www.google.com/search?q={name}')
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # 最初の検索結果のURLを取得
            first_result = soup.find('cite')
            url = first_result.text if first_result else 'URL not found'
        
            # 会社概要を取得（仮の例）
            summary = "Example summary based on additional scraping logic."
        
            # CSVに書き込み
            writer.writerow([name, url, summary])

        # Chromeを閉じる
        driver.quit()

        # 再度Chromeを起動
        driver = webdriver.Chrome(service=service)

# ブラウザを閉じる（最後の処理後にのみ実行）
driver.quit()

print("Completed. The results are saved in 'company_details.csv'.")
