import requests
from bs4 import BeautifulSoup as BS
import os
import csv

diry= str(input("Input name directory: "))
os.mkdir(f"C://Users/79093/Desktop/{diry}")
url = "https://yandex.ru/images/search?text=собаки"
r = (requests.get(url))
soup= BS(r.text, "lxml")
img_url="https:"+soup.find('img',class_="serp-item__thumb justifier__thumb").get("src")
print(img_url)
img_d = requests.get(img_url).content
with open(f'C://Users/79093/Desktop/{diry}/0.jpg','wb') as file:
    file.write(img_d)


#img_op = open('0' + '.jpg', 'wb')
#img_op.write(img.content)
#img_op.close()