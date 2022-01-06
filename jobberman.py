from bs4 import BeautifulSoup
import requests
import re

jobberman_url = requests.get('https://www.jobberman.com/jobs/software-data/lagos?industry=it-telecoms').text
soup = BeautifulSoup(jobberman_url, 'lxml')
page = soup.find('a', class_='page-link')
page_num = int(str(page).split('>')[-2].split('<')[0])
for pages in range(1, page_num+1):
    jobberman_url_new = requests.get(f'https://www.jobberman.com/jobs/software-data/lagos?industry=it-telecoms&page={pages}').text
    soup = BeautifulSoup(jobberman_url_new, 'lxml')
    job_title = soup.find_all('div', class_='relative inline-flex flex-col justify-center w-full') #('h3', class_='text-link text-lg font-medium')
    for job in job_title:
        job_tag = job.find(class_='text-link text-lg font-medium')
        if job_tag is None:
            continue
        job_name = job_tag.text
        date = job.find(class_='ml-auto').text
        job_url = job.div.a['href']
        job_salary = job.find(class_='margin-right--5 text--bold')
        print(job_salary)

        # print(job_name)
        # print(date)
        # print(job_url)
        # print('__________________________')



