from bs4 import BeautifulSoup
import requests
import time

user_skills = input("enter the skill you're familiar with: ")
print(f'filtering out {user_skills}')


def find_jobs():
    html_txt = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_txt, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(jobs)
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.lower()
        if 'few' not in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if user_skills in skills:
                with open(f'job_posts/{index}.txt', 'w') as f:
                    f.write(f'company name: {company_name.strip()}\n')
                    f.write(f'required skills: {skills.strip()}\n')
                    f.write(f'more_info: {more_info}')
                print(f'file saved: {index}')


if __name__ == '__main__':
     find_jobs()
     print('Waiting 10 minutes.....')
     time.sleep(600)

find_jobs()
