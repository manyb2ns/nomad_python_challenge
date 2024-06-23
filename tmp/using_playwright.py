from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

start = time.time()

url = "https://www.kpop-radar.com/"
singer = "SEVENTEEN"

p = sync_playwright().start()
browser = p.chromium.launch().new_page()
browser.goto(f"{url}{singer}")
content = browser.content()
soup = BeautifulSoup(content, "html.parser")

youtube = soup.find('li', id='youtube_today').find("span", class_="total").text
instagram = soup.find("li", id="instagram_today").find("span", class_="total").text
tictok = soup.find("li", id="tiktok_today").find("span", class_="total").text
fancafe = soup.find("li", id="fancafe_today").find("span", class_="total").text

print(f"youtue: {youtube}")
print(f"insta: {instagram}")
print(f"tictok: {tictok}")
print(f"fancafe: {fancafe}")

browser.close()
p.stop()

end = time.time()

print(f"test2.py 실행시간 = {end - start:.5f}")