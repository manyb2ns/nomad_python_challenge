from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

start = time.time()

url = "https://www.kpop-radar.com/"
singer = "SEVENTEEN"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# 웹 드라이버 초기화
driver = webdriver.Chrome(service=Service(), options=options)
driver.get(f"{url}{singer}")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 원하는 요소 찾기
youtube = soup.find('li', id='youtube_today').find("span", class_="total").text
instagram = soup.find("li", id="instagram_today").find("span", class_="total").text
tictok = soup.find("li", id="tiktok_today").find("span", class_="total").text
fancafe = soup.find("li", id="fancafe_today").find("span", class_="total").text

print(f"youtue: {youtube}")
print(f"insta: {instagram}")
print(f"tictok: {tictok}")
print(f"fancafe: {fancafe}")

# 브라우저 닫기
driver.quit()

end = time.time()

print(f"test2.py 실행시간 = {end - start:.5f}")