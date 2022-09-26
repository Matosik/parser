import json
import os
import requests
from bs4 import BeautifulSoup
import time

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
def save_img(img_data,subdir,image_number):
     with open(f'dataset/{subdir}/{str(image_number).zfill(4)}.jpg','wb') as file:
                file.write(img_data)
def create_file(subdir):
    if not os.path.exists(f'dataset/{subdir}'):
        os.makedirs(f'dataset/{subdir}')
def search_images(subdir):
    create_file(subdir)
    page_number=0
    image_number=1
    while True:
        url=f'https://yandex.ru/images/search?p={page_number}&text={subdir}&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image'
        time.sleep(2)
        response=requests.get(url,headers=headers).text
        soap= BeautifulSoup(response,"html.parser")
        links=soap.find_all("img",class_="serp-item__thumb justifier__thumb")
        for link in links:
            link = link.get("src")
            urls='https:'+ link
            img_data=requests.get(urls,verify=False).content
            save_img(img_data,subdir,image_number)
            image_number+=1
            print(f'изображение {str(image_number).zfill(4)}.jpg успешно скачено')
        page_number+=1 
        if image_number>100:
            break    
def main():
    print('Hello')
    search_images('cat')
    search_images('dog')
    print('byе')
    
if __name__ == '__main__':
    main()

