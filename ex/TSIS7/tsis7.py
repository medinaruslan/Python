import pygame
import sys

pygame.init()

win_size = (800, 600)
screen = pygame.display.set_mode(win_size, pygame.RESIZABLE) #создала дисплэй, который можно изменять (увеличивать/уменьшать)
pygame.display.set_caption('Animate a shape') 

background_image = pygame.image.load("background.jpg") #добавила бэкграунд 
background_image = pygame.transform.scale(background_image, win_size)  #бэкграунд подогнала до уровня окна

#название цветов для применения в будущем
GREEN = (0, 128, 0)
LIGHT_GREEN = (144, 238, 144)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)

radius = 50 #размер круга выбрала небольшой, чтобы были видны изменения
color = LIGHT_BLUE 
pos = [win_size[0] // 2, win_size[1] // 2] #размер круга посередине
speed = 1 #скорость изменения вначале (круг увеличивается сразу после запуска кода с этой скоростью)

clock = pygame.time.Clock() #для частоты обновления экрана

while True: #цикл выполняется пока true
    screen.blit(background_image, (0, 0))   #отображает фон с моим бэкгруанд фото

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #чтобы выйти из анимации
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: #если нажать кнопку верх в ноутбуке, скорость изменения увеличится на 0.1
        speed += 0.1
    elif keys[pygame.K_DOWN]:#если нажать кнопку низ в ноутбуке, скорость изменения уменьшится на 0.1
        speed -= 0.1
        if speed < 0:
            speed = 0
    elif keys[pygame.K_p]:  #если нажать кнопку P в ноутбуке, радиус увеличится на 10, то есть круг увеличится на 10 
        radius += 10
    elif keys[pygame.K_o]:  #если нажать кнопку О в ноутбуке, радиус уменьшится на 10, то есть круг уменьшится на 10 
        radius -= 10
        if radius < 0: #чтобы не было ошибки, если уменьшили до 0, что круга нет он не уменьшал дальше
            radius = 0

    radius += speed #чтобы менять радиус, то есть увеличивать/уменьшать

    if radius >= min(win_size) // 2: #чтобы круг не вышел за пределы видимости
        radius = min(win_size) // 2

    pygame.draw.circle(screen, WHITE, pos, radius) #рисуем круг с определенной позицией и радиусом, тут белые границы круга 
    pygame.draw.circle(screen, LIGHT_GREEN, pos, radius - 10) #рисуем круг с определенной позицией и радиусом, тут светло-зеленые границы круга
    pygame.draw.circle(screen, GREEN, pos, radius - 20) #рисуем круг с определенной позицией и радиусом, тут сам круг уже
    #тут я пыталась сделать круг похожим на землю без добавления фото земли 

    pygame.display.flip() #обновление окна, чтобы мы видели изменения 

    clock.tick(60) #частота обновления окна 60
