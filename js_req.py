from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as bs

search = input('Find: ')

url = f'https://www.pinterest.jp/search/pins/?q={search}&rs=typed'

# инициализировать сеанс
session = HTMLSession()
# делаем HTTP‑запрос и получаем ответ
response = session.get(url)
# выполнить Javascript с таймаутом 20 секунд
response.html.render(timeout=20)
# создаем парсер soup
soup = bs(response.html.html, "html.parser")

images = soup.find_all('img')
print(images)

for i, image in enumerate(images):
    name = image['alt']
    link = image['src'].replace('236x', '564x')
    # link = image['src']
    # название не обязательно там обрабатывать
    with open(f'{search}_pic_{i}.jpg', 'wb') as file:
        im = requests.get(link)
        file.write(im.content)