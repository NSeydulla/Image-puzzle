import pygame
from Tile import Tile
from config import sc

class Game():
    def __init__(self, screen, img):
        self.isBusy = False
        self.sc = screen
        self.img = img
        self.tiles = [Tile(i, img) for i in range(sc.tileNum)]
        self.blank = 15
        self.moveTile(11)
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

    def moveTile(self, index):
        self.tiles[self.blank].initPos(index).blit(self.sc)
        self.tiles[index].initPos(self.blank).blit(self.sc)
        self.tiles[self.blank], self.tiles[index] = self.tiles[index], self.tiles[self.blank]
        self.blank = index

    def onClick(self, x, y):
        index = self.getClickedTile(x, y)
        if index in self.getNeighbor():
            self.moveTile(index)

    def getNeighbor(self, index=None):
        if index is None: index = self.blank
        upper = index-sc.rows
        lower = index+sc.rows
        if lower>=sc.tileNum: lower = -1
        left = (index-1) if index%sc.rows!=0 else -1
        right = (index+1) if (index+1)%sc.cols!=0 else -1
        arr = [upper, lower, left, right]
        return list(filter(lambda n: n if n>=0 else None, arr))