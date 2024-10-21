import pygame
import sys
from Colors import Colors
from Parameters import Params

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

while Params.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(Colors.black)
    pygame.display.flip()
    clock.tick(Params.FPS)

