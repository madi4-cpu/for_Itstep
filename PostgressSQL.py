import psycopg2

# Подключение к БД
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 📌 Создаем таблицу товаров
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price INTEGER NOT NULL
    );
""")
conn.commit()

# 📌 Функция для добавления товара
def add_product(name, price):
    cur.execute("INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;", (name, price))
    conn.commit()
    print(f"✅ Добавлен товар: {name} за {price} руб.")

# 📌 Функция для вывода всех товаров
def show_products():
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    print("\n📋 Список товаров:")
    for p in products:
        print(f"🆔 ID: {p[0]}, 📦 {p[1]}, 💰 {p[2]} руб.")
    if not products:
        print("❌ Товаров нет!")

# 📌 Функция для обновления цены товара
def update_price(product_id, new_price):
    cur.execute("UPDATE products SET price = %s WHERE id = %s;", (new_price, product_id))
    conn.commit()
    print(f"🔄 Цена обновлена для ID {product_id} → {new_price} руб.")

# 📌 Функция для удаления товара
def delete_product(product_id):
    cur.execute("DELETE FROM products WHERE id = %s;", (product_id,))
    conn.commit()
    print(f"🗑️ Товар с ID {product_id} удален.")

# 📌 Тестируем CRUD
add_product("Книга", 500)
add_product("Наушники", 2000)
add_product("Клавиатура", 3500)

show_products()  # Выводим товары

update_price(1, 450)  # Меняем цену книги
delete_product(2)  # Удаляем наушники

show_products()  # Снова выводим товары

# Закрываем соединение
cur.close()
conn.close()
