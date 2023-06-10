import json
import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import lxml
from Logger_3 import logger


url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
words = ['python', 'django', 'flask']

def get_headers():
    return Headers(browser='opera', os='win').generate()

job_html = requests.get(url, headers=get_headers()).text

job_soup = BeautifulSoup(job_html, 'lxml')

articles_list = job_soup.find_all(class_='vacancy-serp-item__layout')

path = 'jobs.csv'
@logger(path)
def sample(date):
    job_data = []
    for article in articles_list:
        link = article.find('a')['href']
        try:
            salary = article.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'}).text
        except:
            salary = 'Нет данных!'
        company = article.find('a', class_='bloko-link bloko-link_kind-tertiary').text
        city = article.find('div',{'data-qa':'vacancy-serp__vacancy-address'}).text.split(',')[0]
        job_data.append({
            'Город': city,
            'Компания': company,
            'Зарплата': salary,
            'Cсылка': link
             })
    return job_data

if __name__ == '__main__':
    art = sample(articles_list)