from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    html_content = file.read()  # Читаем HTML из файла

soup = BeautifulSoup(html_content, 'html.parser')  # Используем html_content для парсинга

print(soup.prettify())  # Выводим отформатированный HTML