from flask import Flask, render_template, request
from scraper.berlinstartupjobs import berlinstartupjobs
from scraper.web3 import web3
from scraper.wework import weworkremotely

app = Flask("JobScrapper")

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    jobs = []
    jobs.extend(berlinstartupjobs(keyword).get_jobs())
    jobs.extend(web3(keyword).get_jobs())
    jobs.extend(weworkremotely(keyword).get_jobs())

    return render_template("search.html", keyword=keyword, jobs=jobs, count=len(jobs))

app.run("0.0.0.0", port=8080, debug=True)