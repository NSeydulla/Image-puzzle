import pygame
def get_img(path):
	img = pygame.image.load(path)
	h = img.get_height()
	w = img.get_width()
	max_height = 600
	if h>max_height:
		img = pygame.transform.scale(img, (w*max_height//h, max_height))
	return img

class sc:
	img = get_img('C:/Games/python/pygame/puzzle image/dog.jpg')
	print('image size:', img.get_width(), img.get_height())
	rows = 4
	cols = 4
	tileNum = rows*cols
	tileWidth = img.get_width()//rows
	tileHeight = img.get_height()//cols
	indent = 2

	h = img.get_height()+indent*(cols-1)
	w = img.get_width()+indent*(rows-1)