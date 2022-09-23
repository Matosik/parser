import requests
from bs4 import BeautifulSoup as BS

def save(link):
    file= link.split("/")[-1]
    print(file)
    pass


url = "https://yandex.ru/images/search?text=собаки"
r = (requests.get(url))
soup= BS(r.text, "lxml")

link_a=("https://yandex.ru" + soup.find('div', class_="serp-item__preview").find('a', class_="serp-item__link").get('href'))
print(link_a,"\n\n\n\n\n\n")
url_img=str(link_a)

r_img=requests.get(url_img)

soupimg=BS(r_img.text,"lxml")
#print(soupimg) 
img=(soupimg.find('img',class_="MMImage-Origin"))  #АААААААААААа
print(img)