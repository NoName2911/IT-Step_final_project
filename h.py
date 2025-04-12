import requests
from bs4 import BeautifulSoup as bs

class DniproM:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def getsite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися на сервер")

    def getinfo(self):
        # ⚠️ Це тестовий список (бо парсер працює нестабільно через динамічний контент)
        catalog = [
            {"Назва": "Кава 'Lavazza'", "Ціна": 219},
            {"Назва": "Чай 'Greenfield'", "Ціна": 89},
            {"Назва": "Цукерки 'Roshen'", "Ціна": 125},
            {"Назва": "Молоко 'Яготинське'", "Ціна": 48},
            {"Назва": "Сир 'President'", "Ціна": 109},
            {"Назва": "Шоколад 'Milka'", "Ціна": 56},
            {"Назва": "Вода 'Моршинська'", "Ціна": 22},
            {"Назва": "Печиво 'Марія'", "Ціна": 39},
            {"Назва": "Сік 'Sandora'", "Ціна": 70},
            {"Назва": "Кетчуп 'Торчин'", "Ціна": 45}
        ]
        return catalog

    def showinfo(self, catalog):
        print("ТОП-10 товарів:")
        for i, item in enumerate(catalog, 1):
            print(f"{i}. {item['Назва']} - {item['Ціна']} грн")
        print("-" * 40)

    def make_order(self, catalog):
        order = []
        while True:
            try:
                choice = int(input("Який товар ви хочете придбати? (введіть номер): "))
                if not 1 <= choice <= len(catalog):
                    print("Невірний номер товару.")
                    continue
                quantity = int(input("Скільки одиниць ви хочете купити?: "))
                product = catalog[choice - 1]
                order.append({
                    "Назва": product["Назва"],
                    "Ціна": product["Ціна"],
                    "Кількість": quantity
                })
            except ValueError:
                print("Введіть числові значення.")
                continue

            more = input("Хочете ще щось? (так/ні): ").strip().lower()
            if more != "так":
                break

        # Виводимо замовлення та рахуємо суму
        print("\nВаше замовлення:")
        total = 0
        for item in order:
            subtotal = item["Ціна"] * item["Кількість"]
            total += subtotal
            print(f"- {item['Назва']}: {item['Кількість']} шт. по {item['Ціна']} грн = {subtotal} грн")

        print(f"\nЗагальна сума покупки: {total} грн")


url = "https://dnipro-m.ua/novynky/"
shop = DniproM(url)
shop.getsite()
catalog = shop.getinfo()
shop.showinfo(catalog)
shop.make_order(catalog)
