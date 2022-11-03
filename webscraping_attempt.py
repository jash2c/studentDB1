from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'

#input('''
    #Welcome to the Web Scraping Proj Alpha WIP

    #Please note that this is a limited program with limited capabilities.

    #Enter the url you wan to scrap: ''')

unfamiliar_skill=input('Enter a skill you are not familiar with: ')
print('Filtering out...')

def find_jobs():
    html_text =requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ = 'job-list-comp-name')
        skills =  job.find('span', class_ = 'srp-skills').text.replace(' ','')
        published_date = job.find('span', class_ = 'sim-posted').text
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'Desktop/{index}.txt','xt') as f:
                f.write(f"Company Name: {company_name}")
                f.write(f"Skills: {skills.strip()}")
                f.write(f"More Info: {more_info}")
                print(f'File Saved: {index}.txt')

        print('')
        
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(600)


