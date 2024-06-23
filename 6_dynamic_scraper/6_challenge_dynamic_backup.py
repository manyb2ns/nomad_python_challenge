from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

p = sync_playwright().start()
browser = p.chromium.launch(headless=False) # default) headless=True
page = browser.new_page()
page.goto("https://www.wanted.co.kr/")

# 검색 버튼 클릭
page.click("button.Aside_searchButton__rajGo")
# page.locator("button.Aside_searchButton__rajGo").click()

# placeholder를 기반으로 input을 찾기 & 문자열 채우기
page.get_by_placeholder("검색어를 입력해 주세요.").fill("DevOps")

# Enter 키 입력
page.keyboard.down("Enter")

# ID 기반으로 anchor를 찾아 클릭
page.click("a#search_tab_position")
time.sleep(2)

for x in range(5):
    # 스크롤 다운을 위해 End 키 입력 반복
    page.keyboard.down("End")
    time.sleep(1)

time.sleep(5)

# 현재 페이지의 HTML 코드 가져오기
content = page.content()
# bs4 인스턴스의 파라미터로 content 입력해 가공 준비 완료 !
soup = BeautifulSoup(content, "html.parser")
jobs = soup.find_all("div", class_="JobCard_container--variant-card__gaJS_")

jobs_db = []

for job in jobs:
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company = job.find("span", class_="JobCard_companyName__N1YrF").text
    url = f"https://www.wanted.co.kr{job.find('a')['href']}"
    reward = job.find("span", class_="JobCard_reward__cNlG5").text

    jobs_db.append(
        {
            "title": title,
            "company": company,
            "reward": reward,
            "url": url
        }
    )

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow([
    "title", "company", "reward", "url"
])

for job in jobs_db:
    writer.writerow(job.values())

# 메모리 누수 방지를 위해 종료
file.close()
p.stop