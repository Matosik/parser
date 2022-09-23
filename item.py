import requests
from bs4 import BeautifulSoup as BS
import os
import csv

id=0
def items_pars(counter, id, obj,directory ):
    url=f"https://yandex.ru/images/search?text={obj}"
    r = (requests.get(url))
    soup= BS(r.text, "lxml")
    img_url=soup.findAll('img',class_="serp-item__thumb justifier__thumb")
    for i in range(counter):
        img="https:"+ img_url[i].get("src")
        img_d=requests.get(img).content
        with open(f'C://Users/79093/Desktop/{directory}/{id}.jpg', "wb") as file:
            file.write(img_d)
            id+=1
    return id

diry= input("Input name directory: ")
amount_dog= int(input("Input amount dog images: "))
amount_cat=40-amount_dog
os.mkdir(f"C://Users/79093/Desktop/{diry}")
dogs="собаки"
cats="кошки"
id=items_pars(amount_dog,id,dogs,diry)
items_pars(amount_cat,id,cats,diry)
