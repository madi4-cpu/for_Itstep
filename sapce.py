
import pygame
import random

# Инициализация pygame
pygame.init()

# Размер экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Заголовок и иконка
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')  # Здесь должна быть иконка для игры
pygame.display.set_icon(icon)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Игрок
player_width = 64
player_height = 64
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_img = pygame.image.load('player.png')  # Здесь должна быть картинка для игрока

# Пули
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Враги
enemy_width = 64
enemy_height = 64
enemy_speed = 3
enemies = []

# Очки
score = 0
font = pygame.font.SysFont("Arial", 32)
winning_score = 500  # Очки для победы

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

# Функция для отрисовки игрока
def draw_player(x, y):
    screen.blit(player_img, (x, y))

# Функция для отрисовки пули
def draw_bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, bullet_width, bullet_height))

# Функция для отрисовки врагов
def draw_enemy(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, enemy_width, enemy_height))

# Функция для отрисовки счета
def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Функция для создания врагов
def create_enemy():
    x = random.randint(0, screen_width - enemy_width)
    y = random.randint(-150, -50)
    enemies.append([x, y])

# Главная игровая логика
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Обновление пуль
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        for enemy in enemies[:]:
            if enemy[0] < bullet[0] < enemy[0] + enemy_width and enemy[1] < bullet[1] < enemy[1] + enemy_height:
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    # Проверка победы
    if score >= winning_score:
        print("Вы победили!")
        running = False

    # Обновление врагов
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemies.remove(enemy)
        if enemy[0] < player_x < enemy[0] + enemy_width and enemy[1] < player_y < enemy[1] + enemy_height:
            running = False

    # Создание врагов
    if random.randint(1, 100) > 98:
        create_enemy()

    # Отображение всего на экране
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    draw_score(score)

    pygame.display.update()

    clock.tick(60)

pygame.quit()