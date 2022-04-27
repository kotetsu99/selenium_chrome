from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Webドライバーパス定義
WEB_DRIVER = 'chromedriver.exe'

# 検索文字列
query = 'test'

# オプション定義
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--lang=ja')
options.add_argument('--window-size=1000,1000')

# ブラウザ起動・ページを開く
driver = webdriver.Chrome(WEB_DRIVER, options=options)
driver.get('https://google.com')

# ブラウザ操作
element = driver.find_element(By.NAME, "q")
element.send_keys(query) 
element.send_keys(Keys.ENTER) 

# ブラウザ操作終了
driver.quit()