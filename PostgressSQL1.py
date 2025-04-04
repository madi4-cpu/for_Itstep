import psycopg2

# Функция подключения к базе
def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

# Инициализация таблицы
def initialize_db():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL,
                    balance INTEGER NOT NULL DEFAULT 0
                );
            """)
            conn.commit()
            print("✅ Таблица users создана или уже существует!")

# CREATE — добавление пользователя (если не существует)
def create_user(name, balance):
    with connect_db() as conn:
        with conn.cursor() as cur:
            # Проверяем, существует ли пользователь
            cur.execute("SELECT id FROM users WHERE name = %s;", (name,))
            user = cur.fetchone()

            if user:
                print(f"⚠ Пользователь {name} уже существует с ID {user[0]}")
                return user[0]

            # Создаём нового пользователя
            cur.execute("INSERT INTO users (name, balance) VALUES (%s, %s) RETURNING id;", (name, balance))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"✅ Пользователь {name} создан с ID {user_id}")
            return user_id

# READ — получение списка пользователей
def read_users():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, balance FROM users ORDER BY id;")
            users = cur.fetchall()
            print("\n📊 Список пользователей:")
            for user in users:
                print(f"🔹 ID: {user[0]}, Имя: {user[1]}, Баланс: {user[2]} руб.")
            return users

# UPDATE — обновление баланса пользователя
def update_balance(user_id, new_balance):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET balance = %s WHERE id = %s;", (new_balance, user_id))
            conn.commit()
            print(f"✅ Баланс пользователя {user_id} обновлён до {new_balance} руб.")

# DELETE — удаление пользователя
def delete_user(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            conn.commit()
            print(f"🗑 Пользователь {user_id} удалён.")

# TRANSFER — перевод средств между пользователями
def transfer_money(sender_name, receiver_name, amount):
    with connect_db() as conn:
        with conn.cursor() as cur:
            try:
                # Получаем ID отправителя
                cur.execute("SELECT id, balance FROM users WHERE name = %s;", (sender_name,))
                sender_data = cur.fetchone()
                if sender_data is None:
                    print(f"❌ Отправитель {sender_name} не найден!")
                    return
                sender_id, sender_balance = sender_data
                
                # Проверяем баланс отправителя
                if sender_balance < amount:
                    print(f"❌ Недостаточно средств у {sender_name}!")
                    return

                # Получаем ID получателя
                cur.execute("SELECT id FROM users WHERE name = %s;", (receiver_name,))
                receiver_data = cur.fetchone()
                if receiver_data is None:
                    print(f"❌ Получатель {receiver_name} не найден!")
                    return
                receiver_id = receiver_data[0]

                # Выполняем перевод
                cur.execute("UPDATE users SET balance = balance - %s WHERE id = %s;", (amount, sender_id))
                cur.execute("UPDATE users SET balance = balance + %s WHERE id = %s;", (amount, receiver_id))
                conn.commit()
                print(f"✅ Перевод {amount} руб. от {sender_name} к {receiver_name} выполнен!")
            except Exception as e:
                conn.rollback()
                print(f"❌ Ошибка перевода: {e}")

# Основной блок для тестирования
if __name__ == "__main__":
    initialize_db()
    
    # Создаём пользователей (или получаем их ID, если они уже есть)
    alexey_id = create_user("Алексей", 2000)
    olga_id = create_user("Ольга", 1500)

    # Выводим список пользователей
    read_users()

    # Переводим 500 рублей от Алексея к Ольге
    transfer_money("Ольга", "Алексей", 1000)

    # Проверяем обновлённый список
    read_users()


import psycopg2
from psycopg2 import sql

def create_tables():
    try:
        conn = psycopg2.connect(
            dbname="postgres",  # Название базы данных
            user="postgres",    # Ваш логин
            password="1234",    # Ваш пароль
            host="localhost",   # Адрес базы данных
            port="5432"         # Порт
        )

        cur = conn.cursor()

        # Создание таблицы пользователей
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                balance INTEGER NOT NULL
            );
        """)

        # Создание таблицы товаров
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                price INTEGER NOT NULL
            );
        """)

        # Создание таблицы заказов
        cur.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER NOT NULL,
                total INTEGER NOT NULL
            );
        """)

        conn.commit()
        print("✅ Таблицы users, products и orders успешно созданы!")

    except Exception as e:
        print("Ошибка при создании таблиц:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def add_sample_data():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Добавление пользователей
        cur.execute("INSERT INTO users (name, email, balance) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING;", ("Иван", "ivan@example.com", 1000))
        cur.execute("INSERT INTO users (name, email, balance) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING;", ("Мария", "maria@example.com", 500))

        # Добавление товаров
        cur.execute("INSERT INTO products (name, price) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;", ("Товар 1", 300))
        cur.execute("INSERT INTO products (name, price) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;", ("Товар 2", 150))

        conn.commit()
        print("✅ Примерные данные добавлены!")

    except Exception as e:
        print("Ошибка при добавлении данных:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def create_order(user_id, product_id, quantity):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Получаем информацию о продукте
        cur.execute("SELECT price FROM products WHERE id = %s;", (product_id,))
        product = cur.fetchone()
        if product:
            price = product[0]
            total = price * quantity

            # Проверяем баланс пользователя
            cur.execute("SELECT balance FROM users WHERE id = %s;", (user_id,))
            balance = cur.fetchone()[0]

            if balance >= total:
                # Обновляем баланс пользователя
                cur.execute("UPDATE users SET balance = balance - %s WHERE id = %s;", (total, user_id))

                # Создаем заказ
                cur.execute("""
                    INSERT INTO orders (user_id, product_id, quantity, total)
                    VALUES (%s, %s, %s, %s);
                """, (user_id, product_id, quantity, total))

                conn.commit()
                print(f"✅ Заказ создан! Общая стоимость: {total} руб.")
            else:
                print("❌ Недостаточно средств на балансе!")

        else:
            print("❌ Продукт не найден!")

    except Exception as e:
        print("Ошибка при создании заказа:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def read_orders():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Чтение заказов
        cur.execute("""
            SELECT o.id, u.name, p.name, o.quantity, o.total
            FROM orders o
            JOIN users u ON o.user_id = u.id
            JOIN products p ON o.product_id = p.id;
        """)

        orders = cur.fetchall()
        if orders:
            print("✅ Заказы:")
            for order in orders:
                print(f"ID: {order[0]}, Пользователь: {order[1]}, Товар: {order[2]}, Количество: {order[3]}, Сумма: {order[4]}")
        else:
            print("❌ Заказы не найдены!")

    except Exception as e:
        print("Ошибка при чтении заказов:", e)

    finally:
        cur.close()
        conn.close()


def update_balance(user_id, new_balance):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Обновление баланса пользователя
        cur.execute("UPDATE users SET balance = %s WHERE id = %s;", (new_balance, user_id))
        conn.commit()
        print(f"✅ Баланс пользователя обновлен! Новый баланс: {new_balance}")

    except Exception as e:
        print("Ошибка при обновлении баланса:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def delete_order(order_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Удаление заказа
        cur.execute("DELETE FROM orders WHERE id = %s;", (order_id,))
        conn.commit()
        print(f"✅ Заказ с ID {order_id} удален!")

    except Exception as e:
        print("Ошибка при удалении заказа:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


# Запуск всех операций
if __name__ == "__main__":
    create_tables()       # Создание таблиц
    add_sample_data()     # Добавление примеров данных
    create_order(1, 1, 2) # Создание заказа
    read_orders()         # Чтение всех заказов
    update_balance(1, 900) # Обновление баланса
    delete_order(0)       # Удаление заказа