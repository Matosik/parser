import requests
from bs4 import BeautifulSoup as BS
import os
import csv
from time import sleep
import random as rand

from selenium import webdriver


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

id=0
def items_pars(counter, id, obj,directory ):
    page=0

    while(counter>0):
        print('Страница === ',page)
        a=rand.random()*10
        sleep(a)
        url=f"https://yandex.ru/images/search?p={page}&text={obj}"
        r = (requests.get(url,headers))
        #if(r.status_code== 200):
        soup= BS(r.text, "lxml")
        b=rand.random()*10
        
        sleep(b)
        img_url=soup.findAll('img',class_="serp-item__thumb justifier__thumb")
        if(len(img_url)!=0):
            page+=1
            for i in range(min(len(img_url),counter)):
                img="https:"+ img_url[i].get("src")

                img_d=requests.get(img).content
                with open(f'C://Users/79093/Desktop/dataset/{directory}/00{id}.jpg', "wb") as file:
                    file.write(img_d)
                    id+=1
                    print(f"====Download file {id} ==== ")
            counter-=len(img_url)
        else:
            print("Вылетела капча")
            sleep(10)
            page+=2
            
    return id

diry= input("Input name directory: ")
amount_dog= int(input("Input amount dog images: "))
amount_cat=2000-amount_dog
os.mkdir(f"C://Users/79093/Desktop/dataset/{diry}")
dogs="собаки"
cats="кошки"
id=items_pars(amount_dog,id,dogs,diry)
items_pars(amount_cat,id,cats,diry)
