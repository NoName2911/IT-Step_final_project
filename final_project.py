from itertools import product

import requests
from bs4 import BeautifulSoup as bs

class DniproM:
    def __init__(self, url):
        self.url = url
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def getsite(self):
        response = requests.get(self.url, headers = self.header)  # Надсилаємо запит
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися на сервер")

    def getinfo(self):
        catalog = []
        ctg = self.soup.find_all("div", class_= "catalog page")

        for i in catalog[0:10]:
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 18378617501 )
            price = i.find("div", class_="product-price__current", id = 18378617501 )
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 56765812101 )
            price = i.find("div", class_="product-price__current", id = 56765812101)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 92517948401 )
            price = i.find("div", class_="product-price__current", id = 92517948401)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 61062990801 )
            price = i.find("div", class_="product-price__current", id = 61062990801)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 13013881801 )
            price = i.find("div", class_="product-price__current", id = 13013881801)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 94321899101 )
            price = i.find("div", class_="product-price__current", id = 94321899101)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 72019362801 )
            price = i.find("div", class_="product-price__current", id = 72019362801)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 53032755101 )
            price = i.find("div", class_="product-price__current", id = 53032755101)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 72405152901 )
            price = i.find("div", class_="product-price__current", id = 72405152901)
            name = i.find("p", class_="product-title__title block-ellipsis block-ellipsis-truncate", id = 62363373601 )
            price = i.find("div", class_="product-price__current", id = 62363373601)

            catalog.append(
                {
                "Назва": "Акумуляторний дриль-шуруповерт", "Ціна": 219,
                "Назва": "Пусковий пристрій-компресор", "Ціна": 89,
                "Назва": "Набір інструментів", "Ціна": 125,
                "Назва": "Насосна станція", "Ціна": 48,
                "Назва": "Акумуляторний верстат для заточування ланцюга", "Ціна": 109,
                "Назва": "Бензопила ланцюгова", "Ціна": 56,
                "Назва": "Акумуляторний тример", "Ціна": 22,
                "Назва": "Котушка на колесах для садового шланга", "Ціна": 39,
                "Назва": "Котушка для садового шланга", "Ціна": 70,
                "Назва": "Набір викруток", "Ціна": 45,
                }

            )

            return catalog
    def shopping(self):
        catalog = self.getinfo()
        shop = True

        while shop:
            catalog = input("Який товар ви хочете придбати? ")

        try:
            quantity = int(input("Скільки одиниць товару ви хочете купити? "))
            print("Скільки ви хочете одиниць купити?")
            purchase = input("Хочете ще щось?")
            if purchase  != "так":
        shop = False

    def snowinfo(self, catalog):

        print("№", "НАЗВА", "ЦІНА", "$")
        print("-" * 50)
        for i in catalog:

            print("\t", i("Назва"), "\t", i("Ціна"))

url = "https://dnipro-m.ua/novynky/"
obj = DniproM(url)
obj.getsite()
catalog = obj.getinfo()
obj.snowinfo(catalog)
obj.shopping()
obj.shopping(catalog)
