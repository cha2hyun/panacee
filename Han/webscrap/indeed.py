import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.find('span').string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find('a')["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find('a')
    if company:
        if company_anchor is not None:
            company = str(company_anchor.stirng)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={0*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for a in results:
            job = extract_job(a)
            jobs.append(job)
    return jobs


def get_jobs():
    last_indeed_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_indeed_page)
    return jobs
