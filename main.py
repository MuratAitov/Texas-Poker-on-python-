import pygame
import random

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Техасский покер')
pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()