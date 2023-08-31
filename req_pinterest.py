import requests
# BeautifulSoup4 (bs4) - это библиотека Python для извлечения данных из файлов HTML и XML.
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt

url = 'https://www.pinterest.jp/search/pins/?q=пчелы&rs=typed'

# делаем запрос по этому URL
r = requests.get(url)
# должно быть 200 при успешном запросе
print(r.status_code)
# print(r.text)
# используем встроенный в Python парсер html.parser.
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)
images = soup.find_all('img')
print(images)

for image in images:
    name = image['alt']
    # link = image['src'].replace('236x', '564x')
    link = image['src']
    # название не обязательно там обрабатывать
    with open(name.replace(' ', '-').translate({ord(',') : None, ord(':') : None, ord('.') : None}) + 'test.jpg', 'wb') as file:
        im = requests.get(link)
        file.write(im.content)

# Однако обратите внимание, что есть некоторые веб‑сайты, которые загружают свои данные с помощью Javascript,
# в этом случае вы должны вместо этого использовать библиотеку requests_html.
# Я уже сделал другой скрипт, который вносит некоторые изменения в исходный и обрабатывает рендеринг Javascript