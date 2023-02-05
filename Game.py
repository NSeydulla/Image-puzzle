import pygame
from Tile import Tile
from config import sc
from time import time
from random import choice as ch

class Game():
    def __init__(self, screen, img):
        #animate params
        self.isBusy = False
        self.animatingTile = None
        self.lastTime = 0

        #main params
        self.sc = screen
        self.img = img
        self.tiles = [Tile(i, img) for i in range(sc.tileNum)]
        self.blank = self.tiles[-1].index
        for i in range(min(sc.tileNum*2, 1000)):
            self.swapTiles(ch(self.getNeighbor()))
        
        for tile in self.tiles:
            tile.blit(self.sc)
        self.start = time()

    def getClickedTile(self, x, y):
        j = x // (sc.tileWidth+sc.indent)
        if x >= sc.tileWidth*(j+1) + sc.indent*j: return
        
        i = y // (sc.tileHeight+sc.indent)
        if y >= sc.tileHeight*(i+1) + sc.indent*i: return
        return int(i*sc.rows+j)

    def swapTiles(self, index):
        self.tiles[self.blank].initPos(index).blit(self.sc)
        self.tiles[index].initPos(self.blank).blit(self.sc)
        self.tiles[self.blank], self.tiles[index] = self.tiles[index], self.tiles[self.blank]
        self.blank = index

    def checkWin(self):
        for i in range(sc.tileNum):
            if i != self.tiles[i].index: return False
        return True

    def animate(self):
        self.tiles[self.blank].blit(self.sc, self.x, self.y)
        t = time()-self.lastTime
        if t<sc.animateTime:
            dt = (t/sc.animateTime)
            self.x = self.tiles[self.animatingTile].x+self.dx * dt
            self.y = self.tiles[self.animatingTile].y+self.dy * dt
            self.tiles[self.animatingTile].blit(self.sc, self.x, self.y)
        else:
            self.swapTiles(self.animatingTile)
            self.animatingTile = None
            self.isBusy = False
            if self.checkWin():
                t = time()-self.start
                print('SOLVED! time:', f'{t//60:.0f} m, {t%60:.2f} s. ({t} s.)')

    def onClick(self, x, y):
        self.isBusy = True
        index = self.getClickedTile(x, y)
        if index in self.getNeighbor():
            self.animatingTile = index
            self.lastTime = time()
            self.dy = self.tiles[self.blank].y - self.tiles[index].y
            self.dx = self.tiles[self.blank].x - self.tiles[index].x
            self.x = self.tiles[index].x
            self.y = self.tiles[index].y
            return
        self.isBusy = False

    def getNeighbor(self, index=None):
        if index is None: index = self.blank
        upper = index-sc.rows
        lower = index+sc.rows
        if lower>=sc.tileNum: lower = -1
        left = (index-1) if index%sc.rows!=0 else -1
        right = (index+1) if (index+1)%sc.rows!=0 else -1
        return [i for i in [upper, lower, left, right] if i>-1]