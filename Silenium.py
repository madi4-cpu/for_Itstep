# class Freddy_Fazbears_Pizzeria:
#     def init(self, name, dough, sauce, filling, price):
#         self.name = name
#         self.dough = dough
#         self.sauce = sauce
#         self.filling = filling
#         self.price = price

#     # Добавим метод, чтобы красиво печатать информацию о пицце
#     def repr(self):
#         return f"{self.name} (Цена: {self.price} KZT)"

# class Pepperoni(Freddy_Fazbears_Pizzeria):
#     def init(self):
#         super().init("Пепперони", "Тесто", "Кетчунез", "Говядина", 6500)

# class BBQPizza(Freddy_Fazbears_Pizzeria):
#     def init(self):
#         # Убрал лишний пробел перед соусом
#         super().init("Барбекю", "Тесто", "Соус Барбекю", "Говядина", 7000)

# class SeaFoodPizza(Freddy_Fazbears_Pizzeria):
#     def init(self):
#         super().init("Дары Моря", "Тесто", "Морской Соус", "Лобстер", 15000)

# # --- Класс заказа (цикл while убран отсюда) ---
# class Order:
#     def init(self):
#         self.items = [] # Список для хранения объектов пицц

#     def add_pizza(self, pizza):
#         self.items.append(pizza)
#         print(f"-> Пицца '{pizza.name}' добавлена в заказ.") # Сообщение для пользователя

#     def price(self):
#         # Этот метод уже написан правильно! Считает сумму цен всех пицц в items
#         return sum(pizza.price for pizza in self.items)

#     def display_order(self):
#         if not self.items:
#             print("Заказ пока пуст.")
#             return
#         print("\n--- Ваш текущий заказ ---")
#         for i, item in enumerate(self.items, 1):
#             print(f"{i}. {item}") # Используем repr из класса пиццы
#         print("------------------------")

# # --- Основная часть программы (взаимодействие с пользователем) ---

# current_order = Order() # Создаем ОДИН объект заказа перед циклом

# while True:
#     # Печатаем меню
#     print("\n--- Меню Пиццерии Фредди Фазбера ---")
#     print(f"1) {Pepperoni().name} ({Pepperoni().price} KZT)")
#     print(f"2) {BBQPizza().name} ({BBQPizza().price} KZT)")
#     print(f"3) {SeaFoodPizza().name} ({SeaFoodPizza().price} KZT)")
#     print("-------------------------------------")
#     print("4) Показать текущий заказ")
#     print("5) Оформить заказ и выйти")
#     print("-------------------------------------")

#     choice_str = input("Введите номер действия: ")

#     try:
#         choice = int(choice_str)

#         if choice == 1:
#             # Создаем ОБЪЕКТ пиццы и добавляем его в заказ
#             pizza_to_add = Pepperoni()
#             current_order.add_pizza(pizza_to_add)

#         elif choice == 2:
#             # Создаем ОБЪЕКТ пиццы и добавляем его в заказ
#             pizza_to_add = BBQPizza()
#             current_order.add_pizza(pizza_to_add)

#         elif choice == 3:
#             # Создаем ОБЪЕКТ пиццы и добавляем его в заказ
#             pizza_to_add = SeaFoodPizza()
#             current_order.add_pizza(pizza_to_add)

#         elif choice == 4:
#             # Показываем текущий состав заказа
#             current_order.display_order()

#         elif choice == 5:
#             # Показываем финальный заказ
#             current_order.display_order()
#             # Вызываем метод price() на НАШЕМ объекте заказа
#             total_cost = current_order.price()
#             print(f"\nИтоговая стоимость заказа: {total_cost} KZT")
#             print("Спасибо за ваш заказ у Фредди!")
#             break # Выходим из цикла while

#         else:
#             print("Неверный номер. Пожалуйста, выберите от 1 до 5.")

#     except ValueError:
#         # Обработка ошибки, если пользователь ввел не число
#         print("Ошибка! Пожалуйста, введите ЧИСЛО от 1 до 5.")



my_dict = {"Macbook" : "Pro", "Developer" : "Nick", "Iphone" : 1}
print(my_dict.items())