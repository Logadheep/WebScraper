import os
import string
import requests
from bs4 import BeautifulSoup


def save_article(sp, name):
    print("souping done")
    if sp.find('div', class_='c-article-body') is not None:
        article_body = sp.find('div', class_='c-article-body').text.strip().encode()
        f = open(name, 'wb')
        f.write(article_body)
        print('done')
        f.close()
    else:
        print('None object returned')


n = int(input())
type_article = input()
list_of_url = []
base_url = 'https://www.nature.com/nature/articles'
titles = []
article_types = []
for i in range(n):
    os.mkdir('Page_' + str(i + 1))

for i in range(n):
    page_url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={i + 1}'
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    page_urls = []
    page_titles = []
    page_types = []
    for j in soup.find_all('li', class_='app-article-list-row__item'):
        page_urls.append('https://www.nature.com' + j.a.get('href'))
        title = j.find('a', class_='c-card__link').text
        title = title.strip(' ').translate(str.maketrans(" ", "_", string.punctuation))
        page_titles.append('Page_' + str(i + 1) + '\\' + title + '.txt')
        article_type = j.find('span', class_='c-meta__type').text
        print(article_type)
        page_types.append(article_type)
    list_of_url.append(page_urls)
    titles.append(page_titles)
    article_types.append(page_types)

print(article_types)
print(titles)
print(list_of_url)
for i in range(len(list_of_url)):
    for j in range(len(list_of_url[i])):
        r = requests.get(list_of_url[i][j])
        soup = BeautifulSoup(r.content, 'html.parser')
        if type_article == article_types[i][j]:
            print(True)
            save_article(name=titles[i][j], sp=soup)
