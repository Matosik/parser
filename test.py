import requests
from bs4 import BeautifulSoup as BS

url = 'https://yandex.ru/images/search?text=собака'

r = (requests.get(url))