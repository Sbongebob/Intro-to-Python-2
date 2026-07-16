import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Color Test")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 0, 0))  # red
    pygame.display.update()

pygame.quit()