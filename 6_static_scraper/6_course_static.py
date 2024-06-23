import requests
from bs4 import BeautifulSoup

class RemoteokSearch:
    def __init__(self, keyword):
        self.keyword = keyword
        self.content = self.get_pages(keyword)
        self.jobs = self.content.find_all("td", class_="company position company_and_position")

    def get_pages(self, keyword):
        url = f"https://remoteok.com/remote-{keyword}-jobs"
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })
        return BeautifulSoup(response.content, "html.parser")
    
    def get_jobs(self):
        for job in self.jobs:
            company_name = job.find('h3', itemprop='name')
            job_title = job.find('h2', itemprop='title')
            location = job.find("div", class_="location")
            url = job.find("a", class_="preventLink")
            
            if company_name:
                print(f"Company  : {company_name.text[1:-1]}")
            if job_title:
                print(f"Title    : {job_title.text[1:-1]}")
            if location:
                print(f"Location : {location.text}")
            if url:
                print(f'URL      : https://remoteok.com{url["href"]}')
            print("\n--------------------------------------\n")

###

python_jobs = RemoteokSearch("python")
flutter_jobs = RemoteokSearch("flutter")
golang_jobs = RemoteokSearch("golang")

python_jobs.get_jobs()
flutter_jobs.get_jobs()
golang_jobs.get_jobs()
