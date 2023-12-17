import pygame

pygame.init()
window = pygame.display.set_mode((800,800))


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

run = True
while run:
    quit_game()

    window.fill((0,0,0))

    pygame.display.update()
