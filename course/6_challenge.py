################## Code Challenge ###################
# keyword = ["flutter", "kotlin", "python"]
# 위 키워드마다 스크래핑하는 함수 생성
# 키워드마다 별도 파일 저장 필요
# 함수로 업데이트를 마친 뒤 객체지향으로 구현해보기
# 객체지향으로 업데이트를 마친 뒤 다른 사이트도 스크래핑 해보기
#####################################################

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

class scraper:
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.jobs_db = []
        
        self.content = self.get_keyword_page(keyword)
        self.get_jobs()
        self.save_csv()
    
    def get_keyword_page(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wanted.co.kr/")        
        
        page.click("button.Aside_searchButton__rajGo")
        page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
        page.keyboard.down("Enter")
        
        page.click("a#search_tab_position")
        time.sleep(2)
        
        for x in range(4):
            page.keyboard.down("End")
        
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        browser.close()
        p.stop()
        
        return soup

    def get_jobs(self):
        jobs = self.content.find_all("div", class_="JobCard_container--variant-card__gaJS_")

        for job in jobs:
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company = job.find("span", class_="JobCard_companyName__N1YrF").text
            url = f"https://www.wanted.co.kr{job.find('a')['href']}"
            reward = job.find("span", class_="JobCard_reward__cNlG5").text

            self.jobs_db.append(
                {
                    "title": title,
                    "company": company,
                    "reward": reward,
                    "url": url
                }
            )

    def save_csv(self):
        file = open(f"{self.keyword}_jobs.csv", "w", encoding="UTF-8-sig")
        writer = csv.writer(file)
        writer.writerow([
            "title", "company", "reward", "url"
        ])
        
        for job in self.jobs_db:
            writer.writerow(job.values())
        
        file.close()
        
    def show_jobs(self):
        for j in self.jobs_db:
            print(j)
        

keywords = ["flutter", "kotlin", "python"]

for k in keywords:
    k = scraper(k)
    k.show_jobs()