import pygame

def get_img(path, indent, rows, cols):
	img = pygame.image.load(path)
	max_w = pygame.display.Info().current_w-indent*(cols-1)
	max_h = pygame.display.Info().current_h-indent*(rows-1)-70
	aspect = max_w/max_h

	h = img.get_height()
	w = img.get_width()
	while (h<max_h) if aspect>1 else (w<max_w):
		img = pygame.transform.scale2x(img)
		h = img.get_height()
		w = img.get_width()
	if (h>max_h) if aspect>1 else (w>max_w):
		img = pygame.transform.scale(img, (w*max_h//h, max_h) if aspect>1 else (max_w, h*max_w//w))
	return img

class sc:
	pygame.init()
	rows = 4
	cols = 4
	tileNum = rows*cols
	indent = 3
	img = get_img('C:/Games/python/pygame/puzzle image/0.jpg', indent, rows, cols)
	print('image size:', img.get_width(), img.get_height())
	
	tileWidth = img.get_width()//rows
	tileHeight = img.get_height()//cols

	animateFrames = 1
	animateCd = (0.3/animateFrames) if animateFrames >1 else 0

	h = img.get_height()+indent*(cols-1)
	w = img.get_width()+indent*(rows-1)