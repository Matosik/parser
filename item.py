import requests
from bs4 import BeautifulSoup as BS
import os
from time import sleep
import random as rand
import cv2
from selenium import webdriver


headers = {"Accept": "*/*","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

id=0


def rewrite (id,diry):
    img = cv2.imread(f'dataset/{diry}/{id}.jpg')
    cv2.imwrite(f'dataset/{diry}/{id}.jpg', img)

def items_pars(counter, id, obj,directory ):
    page=0

    while(counter>0):
        print('Страница === ',page)
        url=f"https://yandex.ru/images/search?p={page}&text={obj}"
        sleep(2)
        r = (requests.get(url,headers))

        soup= BS(r.text, "lxml")

        img_url=soup.findAll('img',class_="serp-item__thumb justifier__thumb")
        if(len(img_url)!=0):
            page+=1
            locale_counter=0
            for i in range(min(len(img_url),counter)):
                img="https:"+ img_url[i].get("src")
                sleep(2)
                img_d=requests.get(img).content
                with open(f'dataset/{directory}/{id}.jpg', "wb") as file:
                    file.write(img_d)
                    print(f"====Download file {id} ==== ")
                    rewrite(id,directory)
                    id+=1
                    locale_counter+=1
            counter-=locale_counter
        else:
            print("Вылетела капча")
            sleep(30)
            page+=2
            
    return "УРА"
query=input("Введите запрос: ")
diry= input(f"Папка для картинок с запросом'{query}': ")
counter_imgg=1100
os.makedirs(f"dataset/{diry}")
print(items_pars(counter_imgg,id,query,diry))