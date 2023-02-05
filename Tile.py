import pygame
from config import sc
from math import ceil

class Tile():
    def __init__(self, index, img):
        self.index = index
        self.initPos(index)
        self.img = img.subsurface((self.x-self.j*sc.indent, self.y-self.i*sc.indent, ceil(sc.tileWidth), ceil(sc.tileHeight)))
        if index == sc.tileNum-1:
            self.img.fill((0,0,0))

    def blit(self, screen, x=None, y=None):
        if x is None: x = self.x
        if y is None: y = self.y
        screen.blit(self.img, (x, y))

    def initPos(self, index):
        self.i = index//sc.rows
        self.j = index%sc.rows
        self.y = int(self.i*sc.tileHeight)+self.i*sc.indent
        self.x = int(self.j*sc.tileWidth)+self.j*sc.indent
        return self