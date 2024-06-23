import requests
from bs4 import BeautifulSoup

class berlinstartupjobs:
    cache = {}

    def __init__(self, keyword):
        self.keyword = keyword
        self.content = self.get_pages(keyword)
        self.jobs = self.content.find_all("li", class_="bjs-jlid")

    def get_pages(self, keyword):
        url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })
        return BeautifulSoup(response.content, "html.parser")

    def get_jobs(self):
        if self.cache.get(self.keyword):
            return self.cache[self.keyword]
        
        jobs = []
        for i in range(len(self.jobs)):
            company_name = self.jobs[i].find('a', class_='bjs-jlid__b')
            job_title = self.jobs[i].find('h4', class_='bjs-jlid__h').find('a')
            url = job_title["href"]

            jobs.append(
                {
                    "company_name": company_name.text,
                    "title": job_title.text,
                    "url": url
                }
            )

        self.cache[self.keyword] = jobs
        return jobs