# from bs4 import BeautifulSoup
# with open('index.html', 'r') as p:
#     c = p.read()
# soup = BeautifulSoup(html_doc, 'html.parser')
# html_doc = """<!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Maggich</title>
#     <link rel="stylesheet" href="./styles.css">
#     <link rel="icon" type="image/png" sizes="32x32" href="https://psv4.userapi.com/c909628/u631833072/docs/d48/a7d8c11577c7/file-fs9mWF7NlqLBL3tvOWslCjta_1.webp">
#     <style>
#         body {
#             margin: 0;
#             padding: 0;
#             background: #2b3e50;
#             font-family: sans-serif;
#             color: #fff;
#             overflow-x: hidden;
#         }

#         html {
#             scroll-behavior: smooth;
#         }

#         canvas {
#             display: block;
#             position: fixed;
#             top: 0;
#             left: 0;
#             z-index: -1;
#             pointer-events: none;
#         }

#         header, footer {
#             z-index: 1;
#         }

#         header {
#             background: rgba(43, 62, 80, 0.8);
#             padding: 20px 0;
#             position: fixed;
#             width: 100%;
#         }

#         .container {
#             max-width: 960px;
#             margin: 0 auto;
#             padding: 0 20px;
#         }

#         .logo {
#             font-size: 24px;
#             font-weight: bold;
#             text-decoration: none;
#             color: #fff;
#         }

#         nav ul {
#             list-style: none;
#             margin: 0;
#             padding: 0;
#             display: flex;
#             justify-content: flex-end;
#         }

#         nav li {
#             margin-left: 20px;
#         }

#         nav a {
#             text-decoration: none;
#             color: #fff;
#             transition: color 0.3s ease;
#         }

#         nav a:hover {
#             color: #f0ad4e;
#         }

#         .register {
#             background: #f0ad4e;
#             color: #fff;
#             padding: 10px 20px;
#             border-radius: 5px;
#         }

#         #hero {
#             background-image: url('путь_к_изображению.jpg');
#             background-size: cover;
#             background-position: center;
#             height: 500px;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             text-align: center;
#         }

#         .hero-text {
#             max-width: 600px;
#             margin: 0 auto;
#         }

#         #hero h2 {
#             font-size: 48px;
#             margin-bottom: 20px;
#         }

#         #hero p {
#             font-size: 18px;
#             margin-bottom: 40px;
#         }

#         .btn {
#             display: inline-block;
#             padding: 15px 30px;
#             background: #f0ad4e;
#             color: #fff;
#             text-decoration: none;
#             border-radius: 5px;
#             font-size: 16px;
#             transition: background-color 0.3s ease;
#         }

#         .btn:hover {
#             background: #d4932e;
#         }

#         #about {
#             padding: 80px 0;
#         }

#         #about h2 {
#             font-size: 36px;
#             margin-bottom: 20px;
#         }

#         #about p {
#             font-size: 16px;
#             line-height: 1.6;
#         }

#         #services {
#             padding: 80px 0;
#             background: #34495e;
#         }

#         #services h2 {
#             font-size: 36px;
#             margin-bottom: 40px;
#         }

#         .service-cards {
#             display: flex;
#             justify-content: space-between;
#         }

#         .service-card {
#             background: #fff;
#             color: #34495e;
#             padding: 40px;
#             border-radius: 10px;
#             text-align: center;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             transition: transform 0.3s ease;
#         }

#         .service-card:hover {
#             transform: translateY(-5px);
#         }

#         .service-card h3 {
#             font-size: 24px;
#             margin-bottom: 20px;
#         }

#         .service-card p {
#             font-size: 16px;
#             line-height: 1.6;
#         }

#         #contact {
#             padding: 80px 0;
#         }

#         #contact h2 {
#             font-size: 36px;
#             margin-bottom: 20px;
#         }

#         #contact p {
#             font-size: 16px;
#             line-height: 1.6;
#             margin-bottom: 40px;
#         }

#         #contact form {
#             display: flex;
#             justify-content: center;
#         }

#         #contact button {
#             background: #f0ad4e;
#             color: #fff;
#             padding: 15px 30px;
#             border: none;
#             border-radius: 5px;
#             font-size: 16px;
#             cursor: pointer;
#             transition: background-color 0.3s ease;
#         }

#         #contact button:hover {
#             background: #d4932e;
#         }

#         footer {
#             background: #34495e;
#             padding: 20px 0;
#             text-align: center;
#         }

#         footer p {
#             font-size: 14px;
#             color: #bdc3c7;
#         }

#         a {
#             color: #f0ad4e;
#             text-decoration: none;
#             transition: color 0.3s ease;
#         }

#         a:hover {
#             color: #d4932e;
#         }

#         h1, h2, h3 {
#             font-weight: bold;
#         }

#         h1 {
#             font-size: 48px;
#         }

#         h2 {
#             font-size: 36px;
#         }

#         h3 {
#             font-size: 24px;
#         }
#     </style>
# </head>
# <body>
# <header>
#     <div class="container">
#         <h1 class="logo">Magamed is the beast teacher ever!</h1>
#         <nav>
#             <ul> 
#                 <li><a href="#about">О нас</a></li>
#                 <li><a href="#services">Услуги</a></li>
#                 <li><a href="#contact">Контакты</a></li>
#                 <li><a href="./register.html" class="register">Зарегистрироваться</a></li>
#             </ul>
#         </nav>
#     </div>
# </header>

# <!-- Canvas для снега -->
# <canvas id="snowCanvas"></canvas>

# <section id="hero">
#     <div class="hero-text">
#         <h2>Создаём уникальные сайты для вашего бизнеса</h2>
#         <p>Качественно, стильно и современно</p>
#         <a href="#contact" class="btn">Связаться с нами</a>
#     </div>
# </section>

# <section id="about" class="container">
#     <h2>О нас</h2>
#     <p>ну что мои студеньтики научу вас как делать такой дизайн сайтов как этот сайт</p>
# </section>

# <section id="services" class="container">
#     <h2>расдел услуг и что я тип предоставляю)</h2>
#     <div class="service-cards">
#         <div class="service-card">
#             <h3>Веб-дизайн</h3>
#             <p>Ну это только после этого мягко говоря (не очень курса)</p>
#         </div>
#         <div class="service-card">
#             <h3>Разработка сайтов</h3>
#             <p>Ну тут beck-end</p>
#         </div>
#         <div class="service-card">
#             <h3>НУУУ тут я не придумал</h3>
#             <p>ладно тогда перейди по этой ссылки что ли. <a target="_blank" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley">сюда жми)</a></p>
#         </div>
        
#     </div>
# </section>

# <section id="contact" class="container">
#     <div>
#         <p>Походу кто то попался)
#         </p>
#     </div>
#     <h2>Контакты</h2>
#     <p>Свяжитесь с нами для обсуждения вашего проекта:</p>
#     <p>Не звоните мне)</p>
    
# </section>

# <footer>
#     <div class="container">
#         <p>Made by Maggich with Maggich ®</p>
#     </div>
# </footer>

# <script>
#     const canvas = document.getElementById("snowCanvas");
#     const ctx = canvas.getContext("2d");

#     canvas.width = window.innerWidth;
#     canvas.height = window.innerHeight;

#     const snowflakes = [];

#     function createSnowflakes() {
#         const x = Math.random() * canvas.width;
#         const y = Math.random() * canvas.height - canvas.height;
#         const radius = Math.random() * 3 + 1;
#         const speed = Math.random() * 2 + 0.5;
#         snowflakes.push({ x, y, radius, speed });
#     }

#     function updateSnowflakes() {
#         snowflakes.forEach((flake, index) => {
#             flake.y += flake.speed;
#             if (flake.y > canvas.height) {
#                 snowflakes.splice(index, 1);
#             }
#         });
#     }

#     function drawSnowflakes() {
#         ctx.clearRect(0, 0, canvas.width, canvas.height);
#         ctx.fillStyle = "white";
#         snowflakes.forEach(flake => {
#             ctx.beginPath();
#             ctx.arc(flake.x, flake.y, flake.radius, 0, Math.PI * 2);
#             ctx.fill();
#         });
#     }

#     function animateSnowfall() {
#         createSnowflakes();
#         updateSnowflakes();
#         drawSnowflakes();
#         requestAnimationFrame(animateSnowfall);
#     }

#     animateSnowfall();
# </script>
# </body>
# </html>"""
# # Открываем HTML-файл
# soup = BeautifulSoup(html_doc, 'html.parser')


# select_element = soup.find_all('section')

# for select in select_element:
#     print(select)

# import time
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://youtube.com")
# driver.save_screenshot('2281337.png')
# time.sleep(5)
# driver.quit()
# driver.refresh()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# # Создаем объект с параметрами для Chrome
# chrome_options = Options()

# # Добавляем аргументы (например, headless-режим)
# chrome_options.add_argument("--headless")  # Запуск без графического интерфейса
# chrome_options.add_argument("--disable-gpu")  # Отключение GPU-ускорения

# # Запускаем Chrome с этими параметрами
# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.google.com")
# print(driver.title)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.get("https://www.ozon.ru/")
time.sleep(5)

# Имитируем ввод в поиск
search_box = driver.find_element(By.NAME, "text")
search_box.send_keys("iPhone 15")
time.sleep(2)
search_box.send_keys(Keys.RETURN)

time.sleep(7)

# Скроллим страницу для эмуляции поведения человека
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
ewsaq   QAWSA   xszaaZSZzazZZAZaaaaaaqq5r4e3e4r43we4r3w2121111111``