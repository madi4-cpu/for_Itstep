# from aiohttp import web

# async def handle(request):
#     return web.Response(text="Hello, World!")  # Возвращаем ответ

# app = web.Application()  # Создаем приложение
# app.add_routes([web.get('/', handle)])  # Настроим маршрут для GET-запросов

# web.run_app(app)  # Запускаем сервер

class Pizza:
    def __init__(self, name, dough, sauce, topping, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.price = price

    def prepare(self):
        print(f"Готовим {self.name}: замешиваем {self.dough}, добавляем {self.sauce} и {self.topping}")

    def bake(self):
        print(f"Выпекаем {self.name}")

    def cut(self):
        print(f"Нарезаем {self.name}")

    def pack(self):
        print(f"Упаковываем {self.name}")

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Пепперони", "Тонкое тесто", "Томатный соус", "Пепперони и сыр", 500)

class BBQPizza(Pizza):
    def __init__(self):
        super().__init__("Барбекю", "Среднее тесто", "BBQ соус", "Курица, сыр, лук", 550)

class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__("Дары Моря", "Толстое тесто", "Белый соус", "Креветки, кальмары, сыр", 600)

class Order:
    def __init__(self):
        self.pizzas = []
        self.total = 0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total += pizza.price

    def calculate_total(self):
        return self.total

class Terminal:
    def __init__(self):
        self.menu = {
            1: PepperoniPizza(),
            2: BBQPizza(),
            3: SeafoodPizza()
        }
        self.order = Order()

    def show_menu(self):
        print("Меню:")
        for num, pizza in self.menu.items():
            print(f"{num}. {pizza.name} - {pizza.price} руб.")

    def take_order(self):
        while True:
            self.show_menu()
            choice = input("Выберите номер пиццы (или '0' для завершения): ")
            if choice == '0':
                break
            if choice.isdigit() and int(choice) in self.menu:
                self.order.add_pizza(self.menu[int(choice)])
                print(f"Добавлена {self.menu[int(choice)].name}")

    def process_payment(self):
        print(f"К оплате: {self.order.calculate_total()} руб.")
        input("Нажмите Enter для оплаты...")
        print("Оплачено! Готовим заказ...")

    def start(self):
        self.take_order()
        self.process_payment()
        print("Заказ принят!")
        
if __name__ == "__main__":
    terminal = Terminal()  
    terminal.start() 