import pygame
from Game import Game
from config import sc
from time import time

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not Game.isBusy:
                Game.onClick(*event.pos)
        if Game.isBusy:
            Game.animate()
            pygame.display.update()
            clock.tick(0)
        else: clock.tick(5)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((sc.w, sc.h))
pygame.display.set_caption("Image puzzle")

Game = Game(screen, sc.img)

pygame.display.update()
main()
pygame.quit()