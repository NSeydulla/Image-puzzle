import pygame
from config import sc

class Tile():
    def __init__(self, index, img):
        self.index = index
        self.initPos(index)
        self.img = img.subsurface((self.x, self.y, sc.tileWidth, sc.tileHeight))
        if index == sc.tileNum-1:
            self.img.fill((0,0,0))

    def blit(self, screen):
        screen.blit(self.img, (self.x+self.j*sc.indent, self.y+self.i*sc.indent))

    def initPos(self, index):
        self.index = index
        self.i = index//sc.cols
        self.j = index%sc.rows
        self.y = self.i*sc.tileHeight
        self.x = self.j*sc.tileWidth
        return self