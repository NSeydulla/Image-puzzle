import pygame
from config import sc

class Tile():
    def __init__(self, index, img):
        self.index = index
        self.initPos(index)
        self.img = img.subsurface((self.x-self.j*sc.indent, self.y-self.i*sc.indent, sc.tileWidth, sc.tileHeight))
        if index == sc.tileNum-1:
            self.img.fill((0,0,0))

    def blit(self, screen, x=None, y=None):
        if x is None: x = self.x
        if y is None: y = self.y
        screen.blit(self.img, (x, y))

    def initPos(self, index):
        self.i = index//sc.cols
        self.j = index%sc.rows
        self.y = self.i*sc.tileHeight+self.i*sc.indent
        self.x = self.j*sc.tileWidth+self.j*sc.indent
        return self