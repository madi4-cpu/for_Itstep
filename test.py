import pyodbc

# Параметры подключения
server = 'tcp:имя_сервера.database.windows.net'  # или 'localhost\sqlexpress' для именованного экземпляра, 'myserver, port' для указания порта
database = 'имя_базы_данных'
username = 'имя_пользователя'
password = '1234'

# Строка подключения
cnxn_str = (
    r'DRIVER={MySQL ODBC 8.2 Driver};'  # или Driver 5.3, если 8.2 не установлен
    r'SERVER=localhost;'
    r'UID=root;'
    r'PWD=1234;'  # замените на пароль root пользователя
)

try:
    # Подключение к SQL Server
    cnxn = pyodbc.connect(cnxn_str)
    cursor = cnxn.cursor()

    # Далее можно выполнять SQL запросы
    # cursor.execute("SELECT * FROM your_table")
    # row = cursor.fetchone()
    # print(row)

    # ...

    # Закрытие соединения
    cnxn.close()

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Ошибка базы данных: {sqlstate}")
    print(f"Подробности ошибки: {ex}")