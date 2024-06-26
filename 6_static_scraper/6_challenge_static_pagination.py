import requests
from bs4 import BeautifulSoup
import time

class scraper:
    def __init__(self, url):
        self.url        = url
        self.content    = self.get_page(self.url)
        self.page_count = self.get_page_count(self.content)
        if self.page_count == 0: self.page_count = 1
        self.jobs       = []
                
        for i in range(1, self.page_count+1):
            url     = f"{self.url}page/{i}"
            if i==1: content = self.content
            else: content = self.get_page(url)
            
            self.get_jobs(content)
        
        print(f"{self.url.split('/')[-2]} scraping is complated...")

    def get_page(self, url):
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        })
        content = BeautifulSoup(response.content, 'html.parser')
        
        return content

    def get_page_count(self, content):
        buttons = content.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers")
        
        if len(buttons) == 0:
            return 1
        else:
            return len(buttons)
        
    def get_jobs(self, content):
        jobs = content.find_all("li", class_="bjs-jlid")
        
        for job in jobs:
            self.jobs.append(
                {
                    "Company": job.find("a", class_="bjs-jlid__b").text,
                    "Position": job.find("h4", class_="bjs-jlid__h").text,
                    "Description": job.find("div", class_="bjs-jlid__description").text.strip(),
                    "URL": job.find("h4", class_="bjs-jlid__h").find("a").get("href")
                }
            )
    
    def show_jobs(self):
        for job in self.jobs:
            print("------------------------------------------------------")
            print(f"Company: {job['Company']}")
            print(f"Position: {job['Position']}")
            print(f"Description: {job['Description']}")
            print(f"URL: {job['URL']}")
            print("------------------------------------------------------\n")
    
eg = scraper("https://berlinstartupjobs.com/engineering/")
py = scraper("https://berlinstartupjobs.com/skill-areas/python/")
ts = scraper("https://berlinstartupjobs.com/skill-areas/typescript/")
js = scraper("https://berlinstartupjobs.com/skill-areas/javascript/")

time.sleep(5)
print()

eg.show_jobs()
py.show_jobs()
ts.show_jobs()
js.show_jobs()