# Импортируем необходимые модули pygame, sys и random для создания игры.
import pygame
import sys
import random

# Инициализируем движок Pygame.
pygame.init()

# Устанавливаем размер окна для отображения игры.
win_size = (800, 600)
screen = pygame.display.set_mode(win_size, pygame.RESIZABLE)
# Устанавливаем заголовок окна.
pygame.display.set_caption('Circles')

# Загружаем изображение фона и масштабируем его до размеров окна.
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, win_size)

# Определяем цвета, которые будем использовать в игре.
GREEN = (0, 128, 0)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)

# Задаем начальные параметры игрока (круга).
radius = 50
color = LIGHT_BLUE
pos = [win_size[0] // 2, win_size[1] // 2]
speed = 5
player_circle = pygame.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)

# Создаем список для хранения кругов, которые игрок должен "съесть".
circles = []
# Создаем объект Clock для управления частотой обновления экрана.
clock = pygame.time.Clock()

# Определяем шрифт для отображения счета.
score_font = pygame.font.SysFont(None, 36)

# Функция для создания нового круга со случайными параметрами.
def generate_circle():
    radius = random.randint(10, 50)
    x = random.randint(radius, win_size[0] - radius)
    y = random.randint(radius, win_size[1] - radius)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    speed = random.uniform(0.5, 2)
    return pygame.Rect(x - radius, y - radius, radius * 2, radius * 2), color, speed

# Функция для отображения текущего счета.
def draw_score(score):
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Функция для проверки столкновения игрока с кругами.
def check_collision(player, circles):
    for circle in circles:
        if player.colliderect(circle[0]):
            player_radius = player.width / 2
            circle_radius = circle[0].width / 2
            if player_radius >= circle_radius:
                player.width += circle[0].width
                player.height += circle[0].height
                circles.remove(circle)
            else:
                return True
    return False

# Переменная для отслеживания времени игры.
timer = 0

# Основной игровой цикл.
while True:
    # Очищаем экран и рисуем фон.
    screen.blit(background_image, (0, 0))
    
    # Обработка событий (нажатие клавиш, закрытие окна и т.д.).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш для управления игроком.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_circle.y -= speed
    elif keys[pygame.K_DOWN]:
        player_circle.y += speed
    elif keys[pygame.K_LEFT]:
        player_circle.x -= speed
    elif keys[pygame.K_RIGHT]:
        player_circle.x += speed

    # Проверка выхода игрока за границы окна.
    if player_circle.width >= min(win_size):
        pygame.quit()
        sys.exit()

    # Создание нового круга через определенный интервал времени.
    if timer % 300 == 0:
        new_circle, circle_color, circle_speed = generate_circle()
        circles.append((new_circle, circle_color, circle_speed))

    # Отрисовка и обновление кругов на экране.
    for circle in circles:
        pygame.draw.ellipse(screen, circle[1], circle[0])
        speed_text = score_font.render(str(round(circle[2], 2)), True, WHITE)
        screen.blit(speed_text, (circle[0].centerx - speed_text.get_width() // 2, circle[0].centery - speed_text.get_height() // 2))

        circle[0].x += circle[2]
        circle[0].x = max(circle[0].x, circle[0].width / 2)  
        circle[0].x = min(circle[0].x, win_size[0] - circle[0].width / 2)  
        circle[0].y += circle[2]
        circle[0].y = max(circle[0].y, circle[0].height / 2)  
        circle[0].y = min(circle[0].y, win_size[1] - circle[0].height / 2)  

    # Отрисовка игрока на экране.
    pygame.draw.ellipse(screen, GREEN, player_circle)

    # Проверка столкновений игрока с кругами.
    if check_collision(player_circle, circles):
        pygame.quit()
        sys.exit()

    # Отображение текущего счета.
    draw_score(player_circle.width // 2)

    # Обновление экрана.
    pygame.display.flip()

    # Увеличение счетчика времени.
    timer += 1
    clock.tick(60)
