import pygame, sys
from pygame.locals import *
pygame.init()

HEIGHT = 1280
WIDTH = 720

DISPLAYSURF = pygame.display.set_mode((HEIGHT,WIDTH))

pygame.display.set_caption("Los amantes de los tanques")

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()