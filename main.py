import pygame

pygame.init()

win_width = 500
win_height = 500

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))

font = pygame.font.Font(None, 32)
text = ''
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                text = "Клавишу y нажали"
            if event.key == pygame.K_q:
                text = "Клавишу Q нажали"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                text = "Клавишу y отпустили"
            if event.key == pygame.K_q:
                text = "Клавишу Q отпустили"
    window.fill((205, 92, 92))
    window.blit(font.render(text, True, (0, 0, 0), (255, 255, 255)),(win_width/2, win_height/2))
    pygame.display.update()
    clock.tick(60)
