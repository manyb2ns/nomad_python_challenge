import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

class web3:

    cache = {}

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = f"https://web3.career/{keyword}-jobs?page="
        self.job = []

    def get_jobs(self):
        if self.cache.get(self.keyword):
            return self.cache[self.keyword]
        
        page = 1
        while True:
            try:
                content = self.get_html(f"{self.url}{page}")
                if content.find('h1').text == "404":
                    print("404")
                    return []

                self.jobs = content.find_all("tr", class_="table_row")
                self.get_jobs_in_page()
                if content.find('li', class_="page-item next disabled") == None:
                    page += 1
                    continue
                else:
                    self.cache[self.keyword] = self.job
                    return self.job
            except:
                return []

    def get_html(self, url):
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })
        return BeautifulSoup(response.content, "html.parser")

    def get_jobs_in_page(self):

        for i in range(len(self.jobs)):
            try:
                company_name = self.jobs[i].find('td', class_='job-location-mobile').find('h3')
                job_title = self.jobs[i].find('h2', class_='fs-6 fs-md-5 fw-bold my-primary')
                url = self.jobs[i].find('td', class_='job-location-mobile').find('a')["href"]

                self.job.append(
                    {
                        "company_name": company_name.text,
                        "title": job_title.text,
                        "url": f"https://web3.career/{url}"
                    }
                )
            except:
                continue