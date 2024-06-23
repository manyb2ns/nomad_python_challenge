import requests
from bs4 import BeautifulSoup

class weworkremotely:
    cache = {}

    def __init__(self, keyword):
        self.keyword = keyword
        self.content = self.get_pages(keyword)
        self.jobs = self.content.find_all("li")

    def get_pages(self, keyword):
        url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })
        return BeautifulSoup(response.content, "html.parser")

    def get_jobs(self):
        if self.cache.get(self.keyword):
            return self.cache[self.keyword]
        
        jobs = []
        for i in range(len(self.jobs)):
            try:
                company_name = self.jobs[i].find('span', class_='company')
                job_title = self.jobs[i].find('span', class_='title')
                url = self.jobs[i].find_all("a")[1]["href"]

                jobs.append(
                    {
                        "company_name": company_name.text,
                        "title": job_title.text,
                        "url": f"https://weworkremotely.com{url}"
                    }
                )
            except:
                continue

        self.cache[self.keyword] = jobs
        return jobs