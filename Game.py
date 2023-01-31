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
        self.stepWSize = (sc.tileWidth+sc.indent)//sc.animateFrames
        self.stepHSize = (sc.tileHeight+sc.indent)//sc.animateFrames

        #main params
        self.sc = screen
        self.img = img
        self.tiles = [Tile(i, img) for i in range(sc.tileNum)]
        self.blank = 15

        for i in range(100):
            self.swapTiles(ch(self.getNeighbor()))

        self.initGame()
    
    def initGame(self):
        for tile in self.tiles:
            tile.blit(self.sc)

    def getClickedTile(self, x, y):
        for i in range(sc.cols):
            for j in range(sc.rows):
                yi = i*sc.tileHeight+i*sc.indent
                xj = j*sc.tileWidth+j*sc.indent
                if xj<x<xj+sc.tileHeight and yi<y<yi+sc.tileWidth: return i*sc.rows+j
        return -1

    def swapTiles(self, index):
        self.tiles[self.blank].initPos(index).blit(self.sc)
        self.tiles[index].initPos(self.blank).blit(self.sc)
        self.tiles[self.blank], self.tiles[index] = self.tiles[index], self.tiles[self.blank]
        self.blank = index

    def checkEndAnimate(self, x, j, y, i):
        return ((x>=j) if self.dx>0 else (x<=j)) if self.dx!=0 else ((y>=i) if self.dy>0 else (y<=i))

    def animate(self):
        if time()-sc.animateCd <= self.lastTime: return
        index = self.animatingTile
        self.tiles[self.blank].blit(self.sc, self.x, self.y)
        self.x += self.dx
        self.y += self.dy
        self.tiles[index].blit(self.sc, self.x, self.y)
        self.lastTime = time()
        if self.checkEndAnimate(self.x, self.tiles[self.blank].x, self.y, self.tiles[self.blank].y):
            self.tiles[self.blank].blit(self.sc, self.x, self.y)
            self.isBusy = False
            self.swapTiles(index)
            self.animatingTile = None
            if self.checkWin():
                print('SOLVED!')

    def checkWin(self):
        for i in range(sc.tileNum):
            if i != self.tiles[i].index: return False
        return True

    def onClick(self, x, y):
        index = self.getClickedTile(x, y)
        if index in self.getNeighbor():
            self.isBusy = True
            self.animatingTile = index
            self.lastTime = time()
            self.dy = (self.tiles[self.blank].y - self.tiles[index].y) // sc.animateFrames
            self.dx = (self.tiles[self.blank].x - self.tiles[index].x) // sc.animateFrames
            self.x = self.tiles[index].x
            self.y = self.tiles[index].y

    def getNeighbor(self, index=None):
        if index is None: index = self.blank
        upper = index-sc.rows
        lower = index+sc.rows
        if lower>=sc.tileNum: lower = -1
        left = (index-1) if index%sc.rows!=0 else -1
        right = (index+1) if (index+1)%sc.cols!=0 else -1
        return [i for i in [upper, lower, left, right] if i>-1]