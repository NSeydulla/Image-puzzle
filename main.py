import pygame
from Game import Game
from config import sc
from time import time

def main():
    while 1:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT: return
            elif not Game.isBusy and ((event.type == pygame.MOUSEMOTION and event.buttons[0]) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)):
                Game.onClick(*event.pos)
        if Game.isBusy:
            Game.animate()
            pygame.display.update()
        clock.tick(60)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((sc.w, sc.h))
pygame.display.set_caption("Image puzzle")

Game = Game(screen, sc.img)

pygame.display.update()
main()
pygame.quit()